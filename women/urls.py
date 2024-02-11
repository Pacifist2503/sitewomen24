from django.urls import path, register_converter
from women import views, converters

register_converter(converters.FourDigitYearConverter, "yyyy")

urlpatterns = [
    # path('', views.index, name='home'),
    path('', views.WomenHome.as_view(), name='home'),
    path('about/', views.about, name='about'),
    # path('add_page', views.add_page, name='add_page'),
    path('add_page/', views.AddPage.as_view(), name='add_page'),
    path('contact/', views.Contact.as_view(), name='contact'),

    path('post/<slug:post_slug>', views.ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>', views.WomenCategory.as_view(), name='category'),
    path('tags/<slug:tag_slug>', views.WomenTag.as_view(), name='tag'),
    path('edit/<int:pk>', views.UpdatePage.as_view(), name='edit_page'),
    path('delete/<slug:slug>', views.DeletePage.as_view(), name='delete_page'),

]
