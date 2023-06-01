from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny,IsAuthenticated
from customer.models import *
from customer.serializers import *

class GetCustomerView(APIView):

    def get(self,request):
       instance = Customer.objects.all()
       serializer = GetCustomerSerializer(instance,many=True)
       return Response(serializer.data)
    def post (self,request):
        params=request.data
        print("data >>>>>>>>>",params)
        ser = GetCustomerSerializer(data=params)
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response({"Message":"Save Sucessfully"})

class GetCustomerAddress(APIView):

    def get(self,request):
       instance = CustomerAddress.objects.all()
       serializer = GetAddressSerializer(instance,many=True)
       return Response(serializer.data)
   

class CustomerDetailsAddressView(APIView):

    def get(self,request,pk):
       instance = Customer.objects.filter(id = pk)
       serializer = CustomerDetailsAddressSerializer(instance,many=True)
       return Response(serializer.data)
    