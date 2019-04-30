from django.shortcuts import render, HttpResponse

# Create your views here.
'''Aqui en core se dejarian las que son  staticas 
'''


def home(request):
    return render(request, 'core/home.html') #estatica

def about(request):
    return render(request, 'core/about.html') #estatica


def store(request):
    return render(request, 'core/store.html') #estatica



