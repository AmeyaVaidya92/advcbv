from django import template

register = template.Library()

@register.filter(name='cut')
def cut(value,arg):
    """
    This filter is used to cut the words
    """

    return value.replace(arg,'')

#register.filter('cut',cut)