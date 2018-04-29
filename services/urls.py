from django.urls import path
from . import views

urlpatterns = [
    path('services/', views.serviceView, name="services"),
]
