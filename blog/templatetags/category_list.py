from atexit import register
from django import template
from blog.models import CatagoryModel

register = template.Library()


@register.simple_tag
def category_list():
    categories = CatagoryModel.objects.all()
    return categories
