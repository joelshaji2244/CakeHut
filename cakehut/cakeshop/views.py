from typing import Any
from django.db import models
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views.generic import View,CreateView,FormView,ListView,UpdateView,DetailView
from django.urls import reverse_lazy,reverse
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

from cakeshop.forms import RegistrationForm,LoginForm,CategoryCreateForm,CakeCreateForm,CakeVarientForm,OfferForm
from cakeshop.models import User,Category,Cakes,CakeVarients,Offers

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


class CategoryCreateView(CreateView,ListView):
    template_name = "cakeshop/category_add.html"
    form_class = CategoryCreateForm
    model = Category
    success_url = reverse_lazy("category_add")
    context_object_name = "category"

    def form_valid(self, form):
        messages.success(self.request,"Category Added Successfully")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request,"Failed to add Category")
        return super().form_invalid(form)
    
    # def get_queryset(self):
    #     return Category.objects.filter(is_active=True)
    

def disable_category(request,*args,**kwargs):
    id = kwargs.get("pk")
    Category.objects.filter(id=id).update(is_active=False)
    messages.success(request,"Category Disabled")
    return redirect("category_add")


def enable_category(request,*args,**kwargs):
    id = kwargs.get("pk")
    Category.objects.filter(id=id).update(is_active=True)
    messages.success(request,"Category Enabled")
    return redirect("category_add")


class CakeCreateView(CreateView):
    template_name = "cakeshop/cake_add.html"
    form_class = CakeCreateForm
    model = Cakes
    success_url = reverse_lazy("cake_list")

    def form_valid(self, form):
        messages.success(self.request,"Cake Added Successfully")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request,"Failed to add Cake")
        return super().form_invalid(form)
    

class CakeListView(ListView):
    template_name = "cakeshop/cake_list.html"
    model = Cakes
    context_object_name = "cakes"


def cake_remove(request,*args,**kwargs):
    id = kwargs.get("pk")
    Cakes.objects.filter(id=id).delete()
    return redirect("cake_list")


class CakeUpdateView(UpdateView):
    template_name = "cakeshop/cake_edit.html"
    form_class = CakeCreateForm
    model = Cakes
    success_url = reverse_lazy("cake_list")


class CakeVarientCreateView(CreateView):
    template_name = "cakeshop/cakevarient_add.html"
    form_class = CakeVarientForm
    model = CakeVarients
    success_url = reverse_lazy("cake_list")

    def form_valid(self, form):
        id = self.kwargs.get("pk")
        obj = Cakes.objects.get(id=id)
        form.instance.cake = obj
        messages.success(self.request,"Varient added Successfully")
        return super().form_valid(form)
    

class CakeDetailView(DetailView):
    template_name = "cakeshop/cake_detail.html"
    model = Cakes
    context_object_name = "cake"


class CakeVarientUpdateView(UpdateView):
    template_name = "cakeshop/cakevarient_edit.html"
    form_class = CakeVarientForm
    model = CakeVarients

    def form_valid(self, form):
        messages.success(self.request,"Cake Varient Updated Successfully")
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.error(self.request,"Updation Failed")
        return super().form_invalid(form)
    
    def get_success_url(self):
        obj = self.object.cake
        return reverse("cake_detail",kwargs={"pk":obj.id})
    
def remove_varient(request,*args,**kwargs):
    id = kwargs.get("pk")
    CakeVarients.objects.get(id=id).delete()
    return redirect("cake_list")
    

class OfferAddView(CreateView):
    template_name = "cakeshop/offer_add.html"
    form_class = OfferForm
    model = Offers

    def form_valid(self, form):
        id = self.kwargs.get("pk")
        obj = CakeVarients.objects.get(id=id)
        form.instance.cakevarient = obj
        messages.success(self.request,"Offer added Successfully")
        return super().form_valid(form)
    def get_success_url(self):
        obj = self.object.cakevarient.cake
        return reverse("cake_detail",kwargs={"pk":obj.id})


def remove_offer(request,*args,**kwargs):
    id = kwargs.get("pk")
    offer_object = Offers.objects.get(id=id)
    cake_id = offer_object.cakevarient.cake.id
    offer_object.delete()
    return redirect("cake_detail",pk=cake_id)