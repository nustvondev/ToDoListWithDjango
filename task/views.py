from django.shortcuts import render
from django.http import HttpResponse
import task
# Create your views here.
tasks= ["Check email", 'Reading book','Testing']
def index(request):
    return render(request, 'task/index.html', {'tasks': tasks})
def add(request):
    return render(request, 'task/add.html')
    