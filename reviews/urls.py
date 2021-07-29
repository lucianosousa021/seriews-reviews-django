from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('vizualizar/<int:review_id>/', views.vizualizar, name='vizualizar'),
    path('criar', views.criar, name='criar'),
    path('salvar', views.salvar, name='salvar'),
    path('deletar/<int:review_id>/', views.deletar, name='deletar'),
    path('editar/<int:review_id>/', views.editar, name='editar'),
    path('buscar', views.buscar, name='buscar'),
]