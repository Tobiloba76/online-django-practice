from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexPage, name='home'),
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('post/', views.postPage, name='post')
]
