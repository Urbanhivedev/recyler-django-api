# serializers.py
from rest_framework import serializers

from .models import MainUsers, Schools

class MainUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MainUsers
        fields = ('user_id', 'user_name',
        'full_name',
        'address',
        'email',
        'phone_number',
        'password',
        'balance',
        'date_created')


class SchoolSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Schools
        fields = ('school_name',
        'school_id',
        'date_created',
         'address',
         'email',
         'password',
         'phone_number')
       
       
