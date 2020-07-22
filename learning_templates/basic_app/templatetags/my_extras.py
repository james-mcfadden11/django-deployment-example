from django import template

register = template.Library()

@register.filter(name='cut_test')
def cut_test(value, arg):
    """
    this cuts out all values of "arg" from the string
    """
    return value.replace(arg, '')

# register.filter('cut_test', cut_test)
