from django import template

register = template.Library()


@register.simple_tag
def my_media(data):
    if data:
        return f'/media/image/{data}'
    return '#'


@register.simple_tag
def my_get_list(data):

    if data:
        new_string = ', '.join([str(item) for item in data.all()])
        return new_string
    return ''
