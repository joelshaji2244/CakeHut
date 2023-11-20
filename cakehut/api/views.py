from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import authentication
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.generics import ListAPIView,DestroyAPIView
from django.core.exceptions import PermissionDenied

from api.serializers import UserCreationSerializer,CakeSerializer,CartSerializer,OrderSerializer,ReviewSerializer
from cakeshop.models import Cakes,CakeVarients,Carts,Orders,Reviews

# Create your views here.

class UserCreationView(APIView):
    def post(self,request,*args,**kwargs):
        serializer = UserCreationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
        
class CakeView(ModelViewSet):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    serializer_class = CakeSerializer
    model = Cakes
    queryset = Cakes.objects.all()

    @action(methods=["post"],detail=True)
    def cart_add(self,request,*args,**kwargs):
        vid = kwargs.get("pk")
        varient_obj = CakeVarients.objects.get(id=vid)
        user = request.user
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(cakevarient=varient_obj,user=user)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

    @action(methods=["post"],detail=True)   
    def place_order(self,request,*args,**kwargs):
        vid = kwargs.get("pk")
        varient_obj = CakeVarients.objects.get(id=vid)
        user = request.user
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(cakevarient=varient_obj,user=user)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
        
    @action(methods=["post"],detail=True)
    def review_add(self,request,*args,**kwargs):
        vid = kwargs.get("pk")
        varient_obj = CakeVarients.objects.get(id=vid)
        user = request.user
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(cakevarient=varient_obj,user=user)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
               
class CartListView(ListAPIView):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    serializer_class = CartSerializer
    def get_queryset(self):
        return Carts.objects.filter(user=self.request.user)
    
class CartDeleteView(DestroyAPIView):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    serializer_class = CartSerializer
    queryset = Carts.objects.all()

    def perform_destroy(self, instance):
        if self.request.user == instance.user:
            instance.delete()
        else:
            raise PermissionDenied("permission denied")
        
class OrderListView(ListAPIView):
    
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    serializer_class = OrderSerializer
    def get_queryset(self):
        return Orders.objects.filter(user=self.request.user)
    
class OrderDeleteView(DestroyAPIView):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    serializer_class = OrderSerializer
    queryset = Orders.objects.all()

    def perform_destroy(self, instance):
        if self.request.user == instance.user:
            instance.delete()
        else:
            raise PermissionDenied("permission denied")
        
class ReviewListView(ListAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    serializer_class = ReviewSerializer
    def get_queryset(self):
        return Reviews.objects.filter(user=self.request.user)
    
class ReviewDeleteView(DestroyAPIView):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    serializer_class = ReviewSerializer
    queryset = Reviews.objects.all()

    def perform_destroy(self, instance):
        if self.request.user == instance.user:
            instance.delete()
        else:
            raise PermissionDenied("permission denied")