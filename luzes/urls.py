from django.urls import path
from . import views

urlpatterns = [
    path('luz/<int:luz_id>/<str:action>/', views.controlar_luz, name='controlar_luz'),
    path('luz/<int:luz_id>/brilho/<int:brilho>/', views.set_brilho, name='set_brilho'),
    path('listar_luzes/', views.listar_luzes, name='listar_luzes'),
    path('', views.listar_luzes, name='index'),
]
