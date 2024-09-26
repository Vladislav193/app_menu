
from django.contrib import admin
from .models import Menu, MenuItem

class MenuItemInline(admin.TabularInline):
    """
    Встроенная форма для редактирования элементов меню прямо на странице редактирования меню.
    """
    model = MenuItem
    extra = 1  # Количество пустых строк для добавления новых элементов

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    """
    Админка для меню, с возможностью редактировать элементы меню инлайном.
    """
    inlines = [MenuItemInline]

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    """
    Админка для элементов меню, с фильтрацией по меню и поиском по названию.
    """
    list_display = ('title', 'menu', 'parent', 'order')
    list_filter = ('menu',)
    search_fields = ('title',)