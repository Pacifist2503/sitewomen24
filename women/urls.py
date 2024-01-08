from django.urls import path
from women import views

urlpatterns = [
    path('', views.index),
    path('cats', views.categories),
]
