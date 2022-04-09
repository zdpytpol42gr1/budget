from django import template

register = template.Library()


def sub(value, arg):
    """Subtracks values of two variables"""
    return value - arg


register.filter('sub', sub)
