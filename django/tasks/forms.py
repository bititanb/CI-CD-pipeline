from django import forms
from django.forms.models import inlineformset_factory

from .models import *

#class CategoryForm(forms.ModelForm):
#    class Meta:
#        model = Category
#        fields = '__all__'

class TaskForm(forms.ModelForm):
    categories = forms.ModelChoiceField(queryset=Category.objects.all(), required=False)

    class Meta:
        model = Task
        fields = ('title', 'body', 'categories', 'timeframe', 'category')
        widgets = {
            'body': forms.Textarea(attrs={'rows':1})
        }

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
