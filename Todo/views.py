from asyncio import tasks
import imp
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import TaskForm


# Create your views here.

def list(request):
    tasks = Task.objects.all().order_by('-id')

    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect ('/')

    data = {'tasks':tasks , 'form':form}
    return render(request, 'Todo/list.html',data)



def updateTask(request, pk):
    task = Task.objects.get(id=pk)
    
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect ('/')

    return render(request, 'Todo/update_task.html',{'form':form})



def deleteTask(request, pk):
    item = Task.objects.get(id=pk)
    item.delete()
    return redirect('/')


    








