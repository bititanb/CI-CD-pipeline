from django.core.urlresolvers import reverse_lazy
from django.views import generic
#from django.shortcuts import render

from tasks import models

class TaskList(generic.ListView):
    model = models.Task
    template_name = 'tasks/tasklist.html'
    fields = '__all__'

class TaskAdd(generic.CreateView):
    model = models.Task
    template_name = 'tasks/taskadd.html'
    #fields = ['title', 'is_closed', 'timeframe']
    fields = '__all__'
    success_url = reverse_lazy('tasklist')

class TaskUpdate(generic.UpdateView):
    model = models.Task
    template_name = 'tasks/taskupdate.html'
    fields = '__all__'
    success_url = reverse_lazy('tasklist')

class TaskDelete(generic.DeleteView):
    model = models.Task
    template_name = 'tasks/taskdelete.html'
    success_url = reverse_lazy('tasklist')
