from django import template
from django.db.models import Count

from women import views
from women.models import Category, TagPost

register = template.Library()


@register.simple_tag()
def get_categories():
    return views.cats_db


@register.inclusion_tag("women/list_categories.html")
def show_categories(cat_selected=0):
    # categories = Category.objects.all()
    categories = Category.objects.annotate(total_posts=Count('posts_cat')).filter(total_posts__gt=0)
    return {
        "catselected": cat_selected,
        "cats": categories
    }


@register.inclusion_tag("women/list_tags.html")
def show_all_tag():
    return {"tags": TagPost.objects.annotate(total_posts=Count('posts_tag')).filter(total_posts__gt=0)}
