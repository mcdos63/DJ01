from django.shortcuts import render
from django.http import HttpResponse

from datetime import datetime
# Получить текущее время
current_time = datetime.now().time()

# Create your views here.
def index(request):
    # return render(request, 'main/index.html')
    return HttpResponse("<h1>Hello, ZёMa</h1>")

def test(request):
    return HttpResponse("<h2>TEST, ZёMa</h2>")

def data(request):
    return HttpResponse(f"<h2>DATA, ZёMa. Time: {current_time}</h2>")