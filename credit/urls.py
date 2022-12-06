from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListView.as_view(), name='index'),
    path('<int:pk>/detail/', views.ClientDetailView.as_view(), name='detail'),  
]