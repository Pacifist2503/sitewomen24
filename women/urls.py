from django.urls import path, register_converter
from women import views, converters

register_converter(converters.FourDigitYearConverter, "yyyy")

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('add_page', views.add_page, name='add_page'),
    path('contact', views.contact, name='contact'),
    path('login', views.login, name='login'),
    path('post/<int:post_id>', views.show_post, name='show_post'),

]
