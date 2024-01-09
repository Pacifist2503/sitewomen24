from django.urls import path, register_converter
from women import views, converters

register_converter(converters.FourDigitYearConverter, "yyyy")

urlpatterns = [
    path('', views.index),
    path('cats/<int:cat_id>', views.categories),
    path('cats/<slug:cat_slug>', views.categories_slug),
    path("articles/<yyyy:year>/", views.year_archive),
]
