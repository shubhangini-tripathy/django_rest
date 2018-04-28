from django.contrib.auth.models import User, Group
from rest_framework import serializers

from .models import  BranchDetail
from rest_framework.serializers import ModelSerializer

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')




class BranchDetailSerializer(ModelSerializer):
    class Meta:
        model =  BranchDetail
        fields = [
                'ifsc',
                'bank_id',
                'branch',
                'address',
                'city',
                'district', 
                'state',
                'bank_name'
                ]     
