from django.shortcuts import render

def index(request):
    return render (request, 'mainpage/homePage.html')
# Create your views here.