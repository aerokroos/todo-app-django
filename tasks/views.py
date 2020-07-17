from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, TemplateView
from .models import Task
from django.urls import reverse_lazy

# Create your views here.
class PageView(TemplateView):
     template_name = 'base.html'



class TaskListView(ListView):
     model = Task
     template_name = 'home.html'

class TaskCreateView(CreateView):
     model = Task
     template_name = 'task_new.html'
     fields = ['title','description']
     
class TaskUpdateView(UpdateView):
     model = Task
     fields = ['title', 'description']
     template_name = 'task_edit.html'

class TaskDeleteView(DeleteView):
     model = Task
     template_name = 'task_delete.html'
     success_url = reverse_lazy('home')

     
     