import json

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, viewsets
from .serializers import FlowTypesSerializer, CreatFlowSerializer, FlowSerializer

from .models import FlowTypes, Flow


class FlowTypesApi(generics.ListCreateAPIView):
    queryset = FlowTypes.objects.all()
    serializer_class = FlowTypesSerializer


class FlowTypesUpdate(generics.RetrieveUpdateAPIView):
    queryset = FlowTypes.objects.all()
    serializer_class = FlowTypesSerializer


class CreatFlow(APIView):
    def get(self, request):
        return Response({'get': "data"})

    def post(self, request):
        data = json.loads(request.body)
        serializer = CreatFlowSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        print(serializer.data)
        flow_data = Flow.objects.get(id=serializer.data['id'])
        flow_serializer = FlowSerializer(flow_data, many=False)
        # flow_serializer.is_valid(raise_exception=True)
        return Response({'post': flow_serializer.data})
