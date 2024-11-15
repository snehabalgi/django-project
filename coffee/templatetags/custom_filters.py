from django import template

register = template.Library()

@register.filter
def multiply(value, arg):
    return value * arg

@register.filter(name='add_class')
def add_class(field, css_class):
    """
    Adds a CSS class to a form field widget.
    """
    # Check if the field is a form field and has a widget attribute
    if hasattr(field, 'field') and hasattr(field.field, 'widget'):
        widget = field.field.widget
        current_classes = widget.attrs.get('class', '')
        new_classes = f"{current_classes} {css_class}".strip()
        widget.attrs['class'] = new_classes
    return field
