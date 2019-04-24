from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
    context = {
        "title": "Página Principal",
        "content": "Bem vindo a página principal"
    }
    return render(request,"home_page.html",context)

def about_page(request):
    context = {
        "title": "Página sobre",
        "content": "Bem vindo a página sobre"
    }
    return render(request,"about/view.html",context)

def contact_page(request):
     context = {
        "title": "Página Contato",
        "content": "Bem vindo a página contato"
     }
     return render(request,"contact/view.html",context) 
