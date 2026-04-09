from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),          # home page
    path('student/', views.student),  # student page
]