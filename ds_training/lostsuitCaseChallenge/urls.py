from django.urls import path
from . import views

urlpatterns = [
    path('', views.test0, name='Training-1'),
    path('test1/', views.test1, name='Training-1'),
]
