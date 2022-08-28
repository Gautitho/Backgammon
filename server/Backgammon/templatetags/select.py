from django import template
register = template.Library()

@register.filter
def select(l, i):
    return l[i]