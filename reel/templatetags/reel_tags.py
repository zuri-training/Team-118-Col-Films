"""Template tags for reel app."""

from django import template
from django.utils.safestring import mark_safe

from reel.models import Category


register = template.Library()

@register.simple_tag
def get_category_options() -> str:
    """Returns HTML options elements for all reel categories"""
    categories = Category.objects.all()
    category_options = '<option value="" selected>----------</option>'
    for category in categories:
        category_options += f'''
            <option value="{category.id}">{category}</option>
        '''
    return mark_safe(category_options)
