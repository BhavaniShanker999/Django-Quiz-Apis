from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from .models import User
from rest_framework import generics
from .serializers import UserSerializer
from rest_framework.response import Response


# Create your views here.
class PostUser(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request, fromat=None):
        
        serializer = UserSerializer(data=request.data)
        # print(serializer.)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Success"}, status=status.HTTP_201_CREATED)
        return Response({'message': list(serializer.errors.keys())[0]+' - '+list(serializer.errors.values())[0][0]}, status=status.HTTP_200_OK)

