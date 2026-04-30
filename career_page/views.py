from django.shortcuts import render

def home(request):
    return render(request, 'career_page/home.html', {})
