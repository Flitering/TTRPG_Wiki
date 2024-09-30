from django.urls import path
from . import views

urlpatterns = [
    path('', views.rules_home, name='rules_home'),
]
