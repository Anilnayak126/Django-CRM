from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="",widget=forms.TextInput(attrs={'class':'forms-control','placeholder':'Email Adress'}))
    first_name = forms.CharField(label="",max_length=100,widget=forms.TextInput(attrs={'class':'forms-control','placeholder':'First Name'}))
    last_name = forms.CharField(label="",max_length=100,widget=forms.TextInput(attrs={'class':'forms-control','placeholder':'Last Name'}))


    class Meta: 
        model = User

