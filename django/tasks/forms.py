from django import forms

class TestForm(forms.Form):
    test_field_1 = forms.CharField(label='testfield1', max_length=15)
