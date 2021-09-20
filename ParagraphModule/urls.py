from django.urls import path
from . import views

# Paragraph module urls patterns for navigation

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:user_name>/list/', views.paragraphList, name='parList'),
]