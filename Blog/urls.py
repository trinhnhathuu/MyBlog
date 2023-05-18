from  django.urls import  path
from .models import MyPost
from . import views

urlpatterns = [
    path('<int:id>/',views.detailpost),
    path('search/blog/<int:id>/',views.detailpost),
]
