from django.urls import path
from app import views

urlpatterns = [
    path('show/', views.show, name="index"),
    path('show/<user>/', views.show_cv, name="show_cv")
    ]