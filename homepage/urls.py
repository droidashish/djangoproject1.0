from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('2/', views.second, name='second')
]

