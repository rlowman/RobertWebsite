from django import template

register = template.Library()

@register.filter
def modulo(num):
    return 9 % num
