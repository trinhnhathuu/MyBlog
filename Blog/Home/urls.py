from  django.urls import  path

from . import views

urlpatterns = [
    path('',views.index),
    path('contact',views.contact),
    path('info',views.info),
    path('blog',views.blog),
    path('/', views.search, name='search'),
    path('create/', views.create_mypost, name='create_mypost'),
    path('register/', views.register, name='register'),
]