from django.urls import path
from . import views

urlpatterns = [
    path('', views.character_list, name='character_list'),
    path('create/', views.create_character, name='create_character'),
    path('<int:id>/', views.character_detail, name='character_detail'),
    path('<int:id>/edit/', views.edit_character, name='edit_character'),
    path('<int:id>/delete/', views.delete_character, name='delete_character'),
]
