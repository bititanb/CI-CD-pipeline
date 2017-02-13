from django.core.urlresolvers import reverse_lazy
from django.views import generic
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
import extra_views

from .models import *
from .forms import *
from .middleware import *


class TaskList(LoginRequiredMixin, extra_views.ModelFormSetView):
    template_name = 'tasks/tasklist.html'
    model = Task
    form_class = TaskForm
    formset_class = TaskModelFormSet
    extra = 1
    can_delete = True

    def get_context_data(self, **kwargs):
        context = super(TaskList, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.filter(user=self.request.user)
        return context

    def get_queryset(self):
        if self.kwargs['slug'] == 'all':
            return Task.objects.filter(user=self.request.user).order_by('timeframe', 'category')
        if self.kwargs['slug'] == 'uncategorized':
            return Task.objects.filter(category=None, user=self.request.user).order_by('timeframe', 'category')
        else:
            category = get_object_or_404(Category, pk__iexact=self.kwargs['pk'])
            return Task.objects.filter(category=category, user=self.request.user).order_by('timeframe', 'category')


class CategoryList(LoginRequiredMixin, extra_views.ModelFormSetView):
    model = Category
    template_name = 'tasks/categorylist.html'
    form_class = CategoryForm
    formset_class = CategoryModelFormSet
    extra = 1
    can_delete = True

    # DEBUG
    def get_context_data(self, **kwargs):
        return super(CategoryList, self).get_context_data(**kwargs)

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)
