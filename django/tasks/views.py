from django.core.urlresolvers import reverse_lazy
from django.views import generic
#from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect

from tasks import models, forms

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


class RecipeCreateView(generic.CreateView):
    template_name = 'tasks/recipe_add.html'
    model = models.Recipe
    form_class = forms.RecipeForm
    success_url = 'success/'

    def get(self, request, *args, **kwargs):
        """
        Handles GET requests and instantiates blank versions of the form
        and its inline formsets.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        ingredient_form = forms.IngredientFormSet()
        instruction_form = forms.InstructionFormSet()
        return self.render_to_response(
            self.get_context_data(form=form,
                                  ingredient_form=ingredient_form,
                                  instruction_form=instruction_form))

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance and its inline
        formsets with the passed POST variables and then checking them for
        validity.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        ingredient_form = forms.IngredientFormSet(self.request.POST)
        instruction_form = forms.InstructionFormSet(self.request.POST)
        if (form.is_valid() and ingredient_form.is_valid() and
            instruction_form.is_valid()):
            return self.form_valid(form, ingredient_form, instruction_form)
        else:
            return self.form_invalid(form, ingredient_form, instruction_form)

    def form_valid(self, form, ingredient_form, instruction_form):
        """
        Called if all forms are valid. Creates a Recipe instance along with
        associated Ingredients and Instructions and then redirects to a
        success page.
        """
        self.object = form.save()
        ingredient_form.instance = self.object
        ingredient_form.save()
        instruction_form.instance = self.object
        instruction_form.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, ingredient_form, instruction_form):
        """
        Called if a form is invalid. Re-renders the context data with the
        data-filled forms and errors.
        """
        return self.render_to_response(
            self.get_context_data(form=form,
                                  ingredient_form=ingredient_form,
                                  instruction_form=instruction_form))
