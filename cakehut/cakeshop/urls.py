from django.urls import path
from cakeshop.views import SignUpView,SignInView,logoutview,CategoryCreateView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name = "signup"),
    path('', SignInView.as_view(), name = "signin"),
    path('logout/', logoutview, name = "signout"),
    path('category_add/', CategoryCreateView.as_view(), name = "category_add"),
]