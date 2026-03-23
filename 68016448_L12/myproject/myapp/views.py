from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from myapp.models import Person

# 1. หน้าแรก (Index) - แสดงรายชื่อประชากรทั้งหมดในตาราง
def index(request):
    all_Person = Person.objects.all()
    return render(request, 'index.html', {"all_person": all_Person})

# 2. หน้าเกี่ยวกับ (About)
def about(request):
    return render(request, 'about.html')

# 3. หน้าฟอร์มสำหรับเพิ่มข้อมูลใหม่ (Form)
def form(request):
    if request.method == "POST":
        # รับค่าจากฟอร์มหน้าเพิ่มข้อมูล
        name = request.POST.get("name")
        age = request.POST.get("age")
        
        # สร้างข้อมูลใหม่ลง Database
        new_person = Person.objects.create(name=name, age=age)
        new_person.save()
        return redirect("/") # บันทึกเสร็จกลับหน้าแรก
        
    return render(request, 'form.html')

# 4. หน้าติดต่อ (Contact)
def contact(request):
    return render(request, 'contact.html')

# 5. ฟังก์ชันแก้ไขข้อมูล (Edit)
def edit(request, person_id):
    # ดึงข้อมูลคนที่จะแก้ไขมาตาม ID
    person = get_object_or_404(Person, pk=person_id)
    
    if request.method == "POST":
        # อัปเดตข้อมูลจากค่าที่พิมพ์ส่งมาใหม่
        person.name = request.POST.get("name")
        person.age = request.POST.get("age")
        person.save() # บันทึกลง Database
        return redirect("/") # แก้ไขเสร็จกลับไปดูผลที่หน้าแรก
    
    # ถ้าไม่ได้กด Submit ให้แสดงหน้าฟอร์มพร้อมข้อมูลเดิม
    return render(request, "edit.html", {"person": person})

# 6. ฟังก์ชันลบข้อมูล (Delete)
def delete(request, person_id):
    person = get_object_or_404(Person, pk=person_id)
    person.delete() # ลบข้อมูลออกจาก Database
    return redirect("/") # ลบเสร็จกลับหน้าแรก