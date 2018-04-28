from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer, BranchDetailSerializer
from .models import BranchDetail 
from rest_framework import generics
#from django_filters.rest_framework import DjangoFilterBackend
#from rest_framework import filters
#from django_filters import rest_framework as filters
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
from django.http import Http404

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CranchDetailViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = BranchDetail.objects.all()
    serializer_class = BranchDetailSerializer




class BranchDetailView(generics.RetrieveAPIView):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    #lookup_field = 'ifsc'
    #ifsc = ifsc.upper()
    #queryset = BranchDetail.objects.all()
    #serializer_class = BranchDetailSerializer

    #lookup_field = 'ifsc'
    serializer_class = BranchDetailSerializer

    def get_queryset(self):
        lookup_field = 'pk'
        pk = self.kwargs['pk'] 
        return BranchDetail.objects.filter(pk__iexact=pk)


class BranchListView(generics.ListAPIView):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    #queryset = BranchDetail.objects.all()
    serializer_class = BranchDetailSerializer
    #filter_backends = (DjangoFilterBackend,)
    #filter_backends = (filters.DjangoFilterBackend,)
    #filter_fields = ('branch_name', 'city')

    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        bank_name = self.request.GET.get('bank_name', None);
        city = self.request.GET.get('city', None);
        if not (bank_name and city):
            # raise ParseError('Bad')
            raise Http404
            # return HttpResponse(status=400)
            # content = {'please move along': 'nothing to see here'}
            # return Response(data="object not found", status=status.HTTP_400_BAD_REQUEST)
        else:
            city, bank_name = city.upper(), bank_name.upper()
            return BranchDetail.objects.filter(bank_name=bank_name, city=city)
