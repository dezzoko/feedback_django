from django import template
from feedbackapp.models import *

register = template.Library()


# @register.simple_tag()
# def get_categories(filter=None):
#     if not filter:
#         return Category.objects.all(pk=filter)
#     return Category.objects.filter(pk=filter)


@register.inclusion_tag('feedback/tag_templates/list_categories.html')
def show_categories(cat_selected=0):
    cats = Category.objects.all()
    return {'cats': cats, 'cat_selected': cat_selected}
