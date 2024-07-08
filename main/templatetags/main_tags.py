from django import template

register = template.Library()


@register.simple_tag
def my_media(data):
    if data:
        return f'/media/image/{data}'
    return '#'

