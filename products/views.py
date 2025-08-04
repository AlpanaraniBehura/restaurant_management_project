from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Item
from .serializers import ItemSerializer

'''
NOTE: Conside this as a reference and follow this same coding structure or format to work on you tasks
'''

# Create your views here.
class ItemView(APIView):

    def get(self, request):
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# Static hardcoded menu
class MenuAPIView(APIView):
    def get(self, request):
        menu = [
            {
                "name": "Veggie Burger",
                "description": "Grilled plant based patty with lettue,tomato and aioil",
                "price":7.49

            },
            {
               "name":"Caesar Salad",
               "description":"Romaine lettuce,parmesan cheese,croutons and Caesar dressing",
               "price": 5.99
            },
            {
                "name":"Margherita Pizza",
                "description":"Classic cheese and tomato pizza with fresh basil"
                "price":8.99
            }
        ]
        return response(menu)
# Dynamic menu using item model
class ItemView(APIView):
    def get(self, request):
        items=Item.objects.all()
        serializer = ItemSerializer(items,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ItemSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
             




