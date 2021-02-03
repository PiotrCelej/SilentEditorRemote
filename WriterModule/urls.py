from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:doc_id>/', views.docInfo, name='docInfo'),
    path('<int:doc_id>/read', views.docRead, name='docRead'),
    path('<int:doc_id>/write', views.getTextBody, name='getTextBody'),
    path('<str:user_name>/list', views.docList, name='docList'),
]