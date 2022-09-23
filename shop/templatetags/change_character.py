from django import template

register = template.Library()

@register.filter
def change_character(value):
    return value.replace(',', '<br>')