from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    edad = forms.IntegerField(required=True, min_value=1,max_value=120,help_text="Tu edad chaval")
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2','edad']