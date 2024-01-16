from django import template

from women import views
from women.models import Category, TagPost

register = template.Library()


@register.simple_tag()
def get_categories():
    return views.cats_db


@register.inclusion_tag("women/list_categories.html")
def show_categories(cat_selected=0):
    categories = Category.objects.all()
    return {
        "catselected": cat_selected,
        "cats": categories
    }


@register.inclusion_tag("women/list_tags.html")
def show_all_tag():
    return {"tags": TagPost.objects.all()}
