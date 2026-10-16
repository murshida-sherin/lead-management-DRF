from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView,RetrieveAPIView,DestroyAPIView,UpdateAPIView,ListAPIView
from rest_framework import authentication,permissions
from LeadApp.serializer import LeadSerializer
from LeadApp.models import Lead
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter

# Create your views here.
class LeadCreateListView(CreateAPIView,ListAPIView):
    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    serializer_class=LeadSerializer
    queryset=Lead.objects.all()
    
    filter_backends=[
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter
    ]
    filterset_fields=['source','status']
    search_fields=['name','email','source','status']
    ordering_fields=['name','added_date']
   
    
class LeadRetrieveUpdateDeleteView(RetrieveAPIView,DestroyAPIView,UpdateAPIView,ListAPIView):
    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    serializer_class=LeadSerializer
    queryset=Lead.objects.all()
    # lookup_url_kwarg="id"--if we used any other variables(like 'id') instead using 'pk',in url-the id getting variable.we have to uset this keyword which tellsthe variable name we used  
    
    
    