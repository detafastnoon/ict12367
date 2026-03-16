from django.urls import path
from . import views  # ตรวจสอบบรรทัดนี้ให้ดี

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('form/', views.form, name='form'),
    path('contact/', views.contact, name='contact'),
]