from django import forms
 
class UserForm(forms.Form):
    name = forms.CharField()
    number = forms.CharField()