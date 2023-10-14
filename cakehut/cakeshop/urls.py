from django.urls import path
from cakeshop.views import SignUpView,SignInView,logoutview,CategoryCreateView,disable_category,CakeCreateView,\
    CakeListView,CakeUpdateView,cake_remove


urlpatterns = [
    path('signup/', SignUpView.as_view(), name = "signup"),
    path('', SignInView.as_view(), name = "signin"),
    path('logout/', logoutview, name = "signout"),
    path('category_add/', CategoryCreateView.as_view(), name = "category_add"),
    path('<int:pk>/disable', disable_category, name = "disable_category"),
    path('cake/add', CakeCreateView.as_view(), name = "cake_add"),
    path('cake/all', CakeListView.as_view(), name = "cake_list"),
    path('<int:pk>/change', CakeUpdateView.as_view(), name = "cake_edit"),
    path('<int:pk>/remove', cake_remove, name = "cake_delete"),
]