from django import forms
class PlusForm(forms.Form):
    a = forms.IntegerField()
    b = forms.IntegerField()
