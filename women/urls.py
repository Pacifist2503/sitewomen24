from django.urls import path, register_converter
from women import views, converters

register_converter(converters.FourDigitYearConverter, "yyyy")

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('cats/<int:cat_id>', views.categories, name='categories_id'),
    path('cats/<slug:cat_slug>', views.categories_slug, name='categories_slug'),
    path("archive/<yyyy:year>/", views.year_archive, name='year_archive'),
]
