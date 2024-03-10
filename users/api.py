from django.forms import model_to_dict
from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView


