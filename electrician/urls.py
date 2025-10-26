from django.urls import path
from . import views


urlpatterns = [
    path('contacts/', views.contacts, name='contacts'),
    path('about_us/', views.about_us, name='about_us'),
    path('main/', views.main, name='main'),
    path('create_project/', views.create_project, name='create_project'),
]
