from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Person

# 1. หน้าแรก (Index)
def index(request):
    all_Person = Person.objects.all()
    return render(request, 'index.html', {"all_person": all_Person})

# 2. หน้าเกี่ยวกับ (About) - ยุบรวมเหลืออันเดียวที่ดึงข้อมูลด้วย
def about(request):
    all_Person = Person.objects.all() 
    return render(request, 'about.html', {"all_person": all_Person})

# 3. หน้าฟอร์ม (Form)
def form(request):
    return render(request, 'form.html')

# 4. หน้าติดต่อ (Contact) - เพิ่มอันนี้เข้าไปเพื่อให้หาย Error AttributeError
def contact(request):
    return render(request, 'contact.html')