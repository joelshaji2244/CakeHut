from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views.generic import View,CreateView,FormView
from cakeshop.forms import RegistrationForm,LoginForm,CategoryCreateForm
from cakeshop.models import User,Category
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.

class SignUpView(CreateView):
    template_name = "cakeshop/register.html"
    form_class = RegistrationForm
    model = User
    success_url = reverse_lazy("signin")

    def form_valid(self, form):
        messages.success(self.request,"Registed Successfully")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request,"Registration Failed")
        return super().form_invalid(form)
    

class SignInView(FormView):
    template_name = "cakeshop/login.html"
    form_class = LoginForm

    def post(self,request,*args,**kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            uname = form.cleaned_data.get("username")
            pwd = form.cleaned_data.get("password")
            usr = authenticate(request,username=uname,password=pwd)
            if usr :
                login(request,usr)
                messages.success(request,"Logedin successfully")
                return redirect("category_add")
            else:
                messages.error(request,"Login Failed")
                return render(request,self.template_name,{"form":form})
        else:
            return render(request,self.template_name,{"form":form})
        

def logoutview(request,*args,**kwargs):
    logout(request)
    return redirect("signin")


class CategoryCreateView(CreateView):
    template_name = "cakeshop/category_add.html"
    form_class = CategoryCreateForm
    model = Category
    success_url = reverse_lazy("category_add")

    def form_valid(self, form):
        messages.success(self.request,"Category Added Successfully")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request,"Failed to add Category")
        return super().form_invalid(form)
    

