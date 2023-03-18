from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .models import Task

# Create your views here.
class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')





class TaskList(ListView):
    model= Task
    #Changing objecty_list name which was giving django by default.
    context_object_name = 'Task'

#After clicking the task user can see details 
class TaskDetail(DetailView):
    model=Task
    context_object_name='task'
    template_name = 'base/task.html'

class TaskCreate(CreateView):
    model=Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')

class TaskUpdate(UpdateView):
    model=Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')
class TaskDelete(DeleteView):
    model=Task
    context_object_name = 'tasks'
    success_url = reverse_lazy('tasks')
    