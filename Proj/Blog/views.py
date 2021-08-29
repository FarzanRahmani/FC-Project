from django.shortcuts import render
from django.http.response import HttpResponse 
from .models import * 
#from .models import User

# Create your views here.

def art(request):
    return render(request,'first_page.html')

def books(request):
    if request.method == "GET" :
        l = books_user.objects.all()
        dic  = {"data": l} 
        return render(request,'books.html',context = dic)
    if request.method == "POST" :
        books_user.objects.create(name= request.POST["b_username"],book= request.POST["b_b"],author= request.POST["b_a"])
        l = books_user.objects.all()
        dic  = {"data": l} 
        return render(request, 'books.html',context = dic)

def poems(request):
    if request.method == "GET" :
        l = poems_user.objects.all()
        dic  = {"data": l}                
        return render(request,'poems.html',context = dic)
    if request.method == "POST" :
        poems_user.objects.create(name= request.POST["p_username"],poem= request.POST["p_p"],poet= request.POST["p_pt"])
        l = poems_user.objects.all()
        dic  = {"data": l} 
        return render(request, 'poems.html',context = dic)

def musics(request):
    if request.method == "GET" :
        l = musics_user.objects.all()
        dic  = {"data": l} 
        return render(request,'musics.html',context = dic)
    if request.method == "POST" :
        musics_user.objects.create(name= request.POST["m_username"],music= request.POST["m_m"],singer= request.POST["m_s"])
        l = musics_user.objects.all()
        dic  = {"data": l} 
        return render(request, 'musics.html',context = dic)





            
