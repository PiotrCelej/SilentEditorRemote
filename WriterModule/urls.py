from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:doc_id>/', views.docRead, name='docRead'),
    path('<str:user_name>/', views.docList, name='docList'),
]