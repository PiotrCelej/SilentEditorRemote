from django.urls import path
from . import views

# Paragraph module urls patterns for navigation

urlpatterns = [
    path('', views.index, name='index'),
]