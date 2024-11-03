from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Presentes
# Create your views here.

def home(request):
    if request.method == 'GET':
     return render(request, 'home.html')
    elif request.method == 'POST':
     nome_presente = request.POST.get('nome_presente')
     preco = request.POST.get('preco')
     importancia = int(request.POST.get('importancia'))
     foto = request.FILES.get('foto')
     if importancia < 1 or importancia > 5:
       return redirect('home')
     presentes = Presentes(
       nome_presente = nome_presente,
       preco = preco,
       importancia = importancia,
       )
     presentes.save()
    
     return redirect("home")
    
    #1:42 DA SEGUNDA AULA 