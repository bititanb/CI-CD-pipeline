from django import forms
from django.forms.formsets import DELETION_FIELD_NAME

from .models import *

_current_user = None

class TaskForm(forms.ModelForm):
    #categories = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label=None)

    class Meta:
        model = Task
        fields= '__all__'
        widgets = {
            'body': forms.Textarea(attrs={'rows': 1, 'placeholder': ''}),
        }
        labels = {
            'body': 'Task',
            'timeframe': 'Date',
        }

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        try:
            # WORKAROUND can't get current user from form when form is not populated
            global _current_user
            _current_user = Category.objects.filter(user=self.instance.user)
        except:
            pass
        finally:
            self.fields['category'].queryset = _current_user

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields= '__all__'
        labels = {
            'title': 'Category',
        }
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': ''}),
        }


class DeletionFieldLabelEmptyMixin(object):
    def add_fields(self, form, index):
        super(DeletionFieldLabelEmptyMixin, self).add_fields(form, index)
        form.fields[DELETION_FIELD_NAME].label = ''

class TaskModelFormSet(DeletionFieldLabelEmptyMixin, forms.BaseModelFormSet):
    pass

class CategoryModelFormSet(DeletionFieldLabelEmptyMixin, forms.BaseModelFormSet):
    pass


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
