from django.urls import path
from cakeshop.views import SignUpView,SignInView,logoutview,CategoryCreateView,disable_category,remove_category,CakeCreateView,\
    CakeListView,CakeUpdateView,cake_remove,CakeVarientCreateView,CakeDetailView,enable_category,CakeVarientUpdateView,\
    remove_varient,OfferAddView,remove_offer,IndexView,remove_review


urlpatterns = [
    path('signup/', SignUpView.as_view(), name = "signup"),
    path('', SignInView.as_view(), name = "signin"),
    path('logout/', logoutview, name = "signout"),
    path('category_add/', CategoryCreateView.as_view(), name = "category_add"),
    path('<int:pk>/disable', disable_category, name = "disable_category"),
    path('<int:pk>/enable', enable_category, name = "enable_category"),
    path('<int:pk>/remove', remove_category, name = "remove_category"),
    path('cake/add', CakeCreateView.as_view(), name = "cake_add"),
    path('cake/all', CakeListView.as_view(), name = "cake_list"),
    path('<int:pk>/change', CakeUpdateView.as_view(), name = "cake_edit"),
    path('<int:pk>/remove', cake_remove, name = "cake_delete"),
    path('cake/<int:pk>/varient', CakeVarientCreateView.as_view(), name = "add_varient"),
    path('<int:pk>/detail', CakeDetailView.as_view(), name = "cake_detail"),
    path('cake/<int:pk>/varient/change', CakeVarientUpdateView.as_view(), name = "update_varient"),
    path('cake/<int:pk>/varient/remove', remove_varient, name = "varient_delete"),
    path('cake/<int:pk>/varient/offer/add', OfferAddView.as_view(), name = "offer_add"),
    path('cake/<int:pk>/varient/offer/remove', remove_offer, name = "offer_delete"),
    path('cake/<int:pk>/review/remove',remove_review, name="review_delete"),
    path('index', IndexView.as_view(), name = "index"),
]