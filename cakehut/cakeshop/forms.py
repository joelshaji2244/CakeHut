from django import forms
from django.contrib.auth.forms import UserCreationForm
from cakeshop.models import User,Category,Cakes,CakeVarients,Offers

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

class CakeCreateForm(forms.ModelForm):
    class Meta:
        model = Cakes
        fields = "__all__"
        widgets = {
            "name":forms.TextInput(attrs={"class":"text-black"}),
            "description":forms.Textarea(attrs={"class":"text-black"}),
            "category":forms.Select(attrs={"class":"text-black"})
        }

class CakeVarientForm(forms.ModelForm):
    class Meta:
        model = CakeVarients
        exclude = ("cake", )
        widgets = {
            "weight":forms.Select(attrs={"class":"text-black"}),
            "price":forms.TextInput(attrs={"class":"text-black"})
        }

class OfferForm(forms.ModelForm):
    class Meta:
        model = Offers
        exclude = ("cakevarient", )
        widgets = {
            "price":forms.TextInput(attrs={"class":"text-black"}),
            "start_date":forms.DateInput(attrs={"class":"form-control","type":"date"}),
            "due_date":forms.DateInput(attrs={"class":"form-control","type":"date"})
        }