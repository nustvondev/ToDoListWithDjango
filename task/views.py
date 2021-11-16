from os import name
from django.shortcuts import render
from django.http import HttpResponse
import task
from django import forms
from django.http.response import HttpResponseRedirect
from django.http import HttpResponseRedirect
from django.urls import reverse
class AddTaskForm(forms.Form):
    task = forms.CharField(label='Task Name')

def index(request):
    if 'tasks' not in request.session:
        request.session['tasks'] = []
    return render(request, 'task/index.html', {'tasks': request.session['tasks']})
def add(request):
    if request.method == 'POST':
        form= AddTaskForm(request.POST)
        if form.is_valid():
            task= form.cleaned_data['task']
            request.session['tasks']+=[task]
            return HttpResponseRedirect(reverse('task:index'))
        else:
            return render(request, 'task/add.html', {'form': form})
    return render(request, 'task/add.html',{
        'form': AddTaskForm()
    })
    