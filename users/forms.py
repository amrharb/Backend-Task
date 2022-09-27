from django import forms

class UsersForm(forms.Form):
    first_name = forms.CharField(min_length=5,max_length=20)
    last_name = forms.CharField(min_length=5,max_length=20)
    birth_date = forms.DateField()
    email = forms.EmailField(min_length=5,max_length=30)
    password = forms.CharField(min_length=5,max_length=30)