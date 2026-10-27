
from django.urls import path, include
from myapp import views



urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('api/home/', views.api_home, name='api_home'),
    path('api/about/', views.api_about, name='api_about'),
]