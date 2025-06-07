from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # return render(request, 'main/index.html')
    return render(request, 'main/index.html')

def test(request):
    return render(request, 'main/test.html')

def data(request):
    return render(request, 'main/data.html')

def article(request):
    return render(request, 'main/article.html')