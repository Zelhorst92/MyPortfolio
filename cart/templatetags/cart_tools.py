from django import template

register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    """ Calculates the subtotal of multiple of the same service """
    return price * quantity
