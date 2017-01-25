from django.core.urlresolvers import reverse_lazy
from django.views import generic
#from django.shortcuts import render
from django.utils import timezone

from tasks import models

class TaskList(generic.DetailView):
    context_object_name = 'tasks'
    template_name = 'tasks/tasklist.html'
    fields = '__all__'

    def get_queryset(self):
        return models.Task.objects.filter(category=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super(TaskList, self).get_context_data(**kwargs)
        context['categories'] = models.Category.objects.all()
        return context

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
