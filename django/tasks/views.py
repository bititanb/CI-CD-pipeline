from django.core.urlresolvers import reverse_lazy
from django.views import generic
#from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import get_object_or_404

from tasks import models

class TaskList(generic.DetailView):
    context_object_name = 'tasks'
    template_name = 'tasks/tasklist.html'
    fields = '__all__'

    def get_object(self):
        category = get_object_or_404(models.Category, title__iexact=self.kwargs['slug'])
        return models.Task.objects.filter(category=category)

    def get_context_data(self, **kwargs):
        #import pudb; pudb.set_trace()
        #import ipdb; ipdb.set_trace()

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

