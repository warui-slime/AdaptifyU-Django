from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Email','class':"block px-2.5 pb-2.5 pt-4 w-full text-sm text-gray-900 rounded-lg border-1 border-slate-800 appearance-none focus:border-blue-500 peer"}))

    class Meta:
        model= User
        fields = ["username","email","password1","password2"]
        widgets = {
            'username': forms.TextInput(attrs={'placeholder':'Username','class':"block px-2.5 pb-2.5 pt-4 w-full text-sm text-gray-900 rounded-lg border-1 border-slate-800 appearance-none focus:border-blue-500 peer"}),
            'password1': forms.PasswordInput(attrs={'placeholder':'Password','class':"block px-2.5 pb-2.5 pt-4 w-full text-sm text-gray-900 rounded-lg border-1 border-slate-800 appearance-none focus:border-blue-500 peer"}),
        }