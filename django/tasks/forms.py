from django import forms
from django.forms.models import inlineformset_factory

from tasks import models

#class CategoryForm(forms.ModelForm):
#    class Meta:
#        model = models.Category
#        fields = '__all__'

TaskFormSet = inlineformset_factory(models.Category, models.Task, fields='__all__')


    #test_field_1 = forms.CharField(label='testfield1', max_length=15)


#class RecipeForm(forms.ModelForm):
#    class Meta:
#        model = models.Recipe
#        fields = '__all__'
#
#
#IngredientFormSet = inlineformset_factory(models.Recipe, models.Ingredient, fields='__all__')
#InstructionFormSet = inlineformset_factory(models.Recipe, models.Instruction, fields='__all__')
