from django.shortcuts import render
from rest_framework import viewsets
from .serializers import RestaurantSerializer
from .models import Restaurant
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from django.http.response import JsonResponse
from rest_framework.views import APIView
from rest_framework import generics

# Create your views here.
# class based views
# listing and adding restaruants
class get_post_data(APIView):
    def get(self, request, format=None):
        queryset = Restaurant.objects.all()
        serializer = RestaurantSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request, format=None):
        serializer = RestaurantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# updating and deleting restaurants
class edit_delete_data(APIView):
    def get_object(self, pk):
        try:
            return Restaurant.objects.get(pk=pk)
        except Restaurant.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, format=None):
        queryset = self.get_object(pk)
        serializer = RestaurantSerializer(queryset)
        return Response(serializer.data)
    
    def patch(self, request, pk, format=None):
        queryset = self.get_object(pk)
        serializer = RestaurantSerializer(queryset,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        queryset = self.get_object(pk)
        queryset.delete()
        return Response({'Deleted successfully'},status=status.HTTP_204_NO_CONTENT)

    
# class based generic views
# class get_postApi(generics.ListCreateAPIView):
#     queryset = Restaurant.objects.all()
#     serializer_class = RestaurantSerializer

# class edit_deleteApi(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Restaurant.objects.all()
#     serializer_class = RestaurantSerializer

# created as viewset
# class RestaurantViewSet(viewsets.ModelViewSet):
#     queryset = Restaurant.objects.all().order_by('id')
#     serializer_class = RestaurantSerializer

# Function based views
# # listing and adding restaruants
# @api_view(['GET', 'POST'])
# def get_post_data(request):
#     if request.method =='GET':
#         queryset = Restaurant.objects.all()
#         serializer = RestaurantSerializer(queryset, many=True)
#         return Response(serializer.data)

#     elif request.method =='POST':
#         serializer = RestaurantSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             # data["success"]= "update successful"
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# # updating and deleting restaurants
# @api_view(['GET','PUT','DELETE'])
# def edit_delete_data(request):
#         try:
#             restaurant = Restaurant.objects.get(data=data)
#         except Restaurant.DoesNotExist:
#             return JsonResponse(status=status.HTTP_404_NOT_FOUND)
#         if request.method =='PUT':
#             serializer = RestaurantSerializer(restaurant,data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 # data["success"]= "edit successful"
#                 return JsonResponse(serializer.data)
#             return Jsonresponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#         elif request.method =='DELETE':
#             operation = restaurant.delete() 
#             data={}
#             if operation:
#                 data["success"]= "delete successful"
#             else:
#                 data["failure"]= "delete failed"
#             return JsonResponse(data=data)
       


