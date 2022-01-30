from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Tasks,TaskForm
from django.urls import reverse

def index1(request):
    task_apps = Tasks.objects.all() 
    context = {'task_apps': task_apps} 
    return render(request, 'web_design.html', context)

def task(request): 
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index1'))
    else:
        form = TaskForm()

    return render(request, 'task.html', {'form': form})

