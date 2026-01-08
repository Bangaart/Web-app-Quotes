from django import template

register = template.Library()


@register.filter('load_tags')
def load_tags(value):
    return ", ".join([str(tag) for tag in value.all()])
