from django.urls import path
from app import views

urlpatterns = [
    path('show/', views.show_cv)
    ]