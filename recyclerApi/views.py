from django.shortcuts import render

# Create your views here.
# views.py
from rest_framework import viewsets

from .serializers import MainUserSerializer, SchoolSerializer
from .models import MainUsers, Schools


class MainUsersViewSet(viewsets.ModelViewSet):
    queryset = MainUsers.objects.all().order_by('user_name')
    serializer_class = MainUserSerializer

class SchoolViewSet(viewsets.ModelViewSet):
    queryset = Schools.objects.all().order_by('school_name')
    serializer_class = SchoolSerializer