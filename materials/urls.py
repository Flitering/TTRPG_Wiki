from django.urls import path
from . import views

urlpatterns = [
    path('', views.material_list, name='material_list'),
    path('add/', views.add_material, name='add_material'),
    path('<int:id>/', views.material_detail, name='material_detail'),
    path('<int:id>/edit/', views.edit_material, name='edit_material'),
    path('<int:id>/delete/', views.delete_material, name='delete_material'),
]
