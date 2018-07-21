from django.http import HttpResponse
from django.shortcuts import render



def homepage(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['wordcount']
    return render(request, 'count.html', {'post_text': fulltext})

def aboutpage(request):
    return render(request, 'about.html')
