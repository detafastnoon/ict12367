from django.urls import path
from myapp import views # ตรวจสอบชื่อ app (myapp) ให้ตรงกับโปรเจกต์ของคุณนะครับ

urlpatterns = [
    # หน้าหลักและหน้าทั่วไป
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('form/', views.form, name='form'),
    path('contact/', views.contact, name='contact'),

    # ส่วนจัดการข้อมูล (Edit & Delete)
    path('edit/<int:person_id>/', views.edit, name='edit'),
    path('delete/<int:person_id>/', views.delete, name='delete'),
]