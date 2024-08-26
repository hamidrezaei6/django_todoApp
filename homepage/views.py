from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo
from django.contrib import messages
from .forms import TodoCreateForm, TodoUpdateForm


# Create your views here.

def index(requset):
    return render(requset, 'index.html')


def home(request):
    all = Todo.objects.all()
    return render(request, 'home.html', {'todos': all})


# def dynamic_homepage(request, homepage):
#     return HttpResponse(homepage)

def detail(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    return render(request, 'detail.html', {'todo': todo})


def delete(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    messages.success(request, 'عملیات حذف با موفقیت انجام شد', 'success')
    return redirect('home')


def create(request):
    if request.method == 'POST':
        form = TodoCreateForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Todo.objects.create(title=cd['title'], body=cd['body'], created=cd['created'])
            messages.success(request, 'عملیات اضافه کردن با موفقیت انجام شد', 'success')
            return redirect('home')
    else:
        form = TodoCreateForm()
    return render(request, 'create.html', {'form': form})


def update(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    if request.method == 'POST':
        form = TodoUpdateForm(request.POST,instance=todo)
        if form.is_valid():
            form.save()
            messages.success(request,'ذخیره اطلاعات با موفقیت انجام شد','success')
            return redirect('details',todo_id)
    else:
        form = TodoUpdateForm(instance=todo)
    return render(request, 'update.html', {'form': form})
