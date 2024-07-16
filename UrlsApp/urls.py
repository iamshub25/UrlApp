from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('index', views.shorten_url, name='shorten_url'),
    path('<str:short_code>/', views.redirect_original, name='redirect_original'),
    path('',views.show)
]