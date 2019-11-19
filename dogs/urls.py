from django.urls import path, include
from . import views
from django.conf.urls import include, url
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.post_principal, name='principal'),
    path('login/', views.user_login, name="user_login"),
    path('success/', views.success, name="user_success"),
    path('logout/', views.user_logout, name="user_logout"),
    path('add/', views.crear_usuario, name="registro"),
]