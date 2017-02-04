from django import forms
from django.forms.formsets import DELETION_FIELD_NAME


from .models import *

#class CategoryForm(forms.ModelForm):
#    class Meta:
#        model = Category
#        fields = '__all__'

class TaskForm(forms.ModelForm):
    #import pudb; pudb.set_trace()
    #categories = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label=None)

    class Meta:
        model = Task
        fields= '__all__'
        widgets = {
            'body': forms.Textarea(attrs={'rows':1}),
        }
        labels = {
            'body': 'What',
            'timeframe': 'When',
        }

class TaskModelFormSet(forms.BaseModelFormSet):

    def add_fields(self, form, index):
        super(TaskModelFormSet, self).add_fields(form, index)
        #import pudb; pudb.set_trace()
        form.fields[DELETION_FIELD_NAME].label = ''

#TaskFormSet = forms.modelformset_factory(Task, fields='__all__', formset=TaskModelFormSet)

#class TaskInlineFormSet(InlineFormSet):
#    model = Task
#    extra = 2
#    form_class = TaskForm
#    form = TaskForm

#TaskFormSet = inlineformset_factory(Category, Task, fields='__all__')


    #test_field_1 = forms.CharField(label='testfield1', max_length=15)


#class RecipeForm(forms.ModelForm):
#    class Meta:
#        model = Recipe
#        fields = '__all__'
#
#
#IngredientFormSet = inlineformset_factory(Recipe, Ingredient, fields='__all__')
#InstructionFormSet = inlineformset_factory(Recipe, Instruction, fields='__all__')
