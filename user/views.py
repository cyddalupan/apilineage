from django.shortcuts import render
from user.serializer import UserSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer

    @action(detail=False)
    def hello(self, request):
        return Response("hello world")