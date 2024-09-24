from django import template
from app.menu.models import Menu
register = template.Library()


@register.inclusion_tag('menu.html')
def menu(context):
    menu