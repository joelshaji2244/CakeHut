from django.urls import path
from api import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import ObtainAuthToken

router = DefaultRouter()
router.register("cakes",views.CakeView, basename="cakes")

urlpatterns = [

    path('register/', views.UserCreationView.as_view()),
    path('token/', ObtainAuthToken.as_view()),
    path('carts/', views.CartListView.as_view()),
    path('carts/<int:pk>/remove/', views.CartDeleteView.as_view()),
    path('orders/', views.OrderListView.as_view()),
    path('orders/<int:pk>/remove/', views.OrderDeleteView.as_view()),
    path('reviews/', views.ReviewListView.as_view()),
    path('reviews/<int:pk>/remove/', views.ReviewDeleteView.as_view()),

]+router.urls