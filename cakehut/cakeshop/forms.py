from django import forms
from django.contrib.auth.forms import UserCreationForm
from cakeshop.models import User,Category

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username","password1","password2","email","phone","address"]


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget = forms.PasswordInput())

class CategoryCreateForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name"]