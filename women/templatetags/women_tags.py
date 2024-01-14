from django import template

from women import views

register = template.Library()


@register.simple_tag()
def get_categories():
    return views.cats_db


@register.inclusion_tag("women/list_categories.html")
def show_categories(cat_selected=0):
    return {
        "catselected": cat_selected,
        "cats": views.cats_db
    }
