from django.urls import path
from . import views

urlpatterns = [
    path('', views.material_list, name='material_list'),
    path('add/', views.add_material, name='add_material'),
    path('<int:id>/', views.material_detail, name='material_detail'),
]
