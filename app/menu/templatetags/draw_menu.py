from django import template
from django.db.models import Prefetch
from ..models import Menu, MenuItem

register = template.Library()

@register.inclusion_tag('menu/draw_menu.html', takes_context=True)
def draw_menu(context, menu_name):
    """
    Template tag для отрисовки меню по его названию.Загружает меню с элементами,
    фильтрует элементы по родителям и передает в шаблон для рендеринга.

    :param context: Контекст шаблона(для получения текущего URL страницы)

    :param menu_name: Название меню, которое нужно отрисовать
    """
    try:
        request = context['request']  # Получаем текущий запрос
        menu = Menu.objects.prefetch_related(
            Prefetch('items', queryset=MenuItem.objects.filter(parent__isnull=True).select_related('parent'))
        ).get(name=menu_name)

        current_url = request.path  # Получаем текущий URL
        return {
            'menu': build_menu_tree(menu.items.all(), current_url),  # Строим дерево элементов
            'current_url': current_url
        }
    except Menu.DoesNotExist:
        # Если меню с заданным названием не существует, возвращаем пустое меню
        return {'menu': []}

def build_menu_tree(menu_items, current_url, depth=1):
    """
    Рекурсивная функция для построения древовидной структуры меню.
    Возвращает список элементов меню с их дочерними элементами.

    :param menu_items: Список элементов меню верхнего уровня
    :param current_url: Текущий URL страницы
    :param depth: Глубина рекурсии (используется для вложенности)
    """
    menu_tree = []
    for item in menu_items:
        children = item.children.all()  # Получаем детей для каждого элемента меню
        menu_tree.append({
            'item': item,
            'children': build_menu_tree(children, current_url, depth + 1) if children else [],
            'is_active': current_url == item.get_url(),  # Определяем, является ли элемент активным
            'is_parent_active': any(current_url == child.get_url() for child in children)  # Активен ли хотя бы один из детей
        })
    return menu_tree