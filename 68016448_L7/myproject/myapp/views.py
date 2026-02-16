from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request): 
    return HttpResponse("<h1>หน้าแรกของเว็บไซต์วิชา ICT12367</h1>") 

def about(request): 
    return HttpResponse("<h1>เกี่ยวกับเรา</h1>") 

def form(request): 
    return render(request, 'form.html')

def contact(request): 
    return HttpResponse("<h1>ติดต่อ นันทพงศ์</h1>") 