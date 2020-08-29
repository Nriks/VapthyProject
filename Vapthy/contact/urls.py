from django.urls import path
from . import views


urlpatterns = [
    path('formContact/', views.contactView, name='contact'),
    path('success/', views.successView, name='success'),

]
