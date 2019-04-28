from django.shortcuts import render

def tutorial_page(request):
    return render(request, 'tutorial/tutorial.html')
