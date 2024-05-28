from django.contrib import admin
from django.urls import path
from .views import FlowTypesApi, FlowTypesUpdate, CreatFlow

urlpatterns = [
    path('flow-types/', FlowTypesApi.as_view(), name='flow-types'),
    path('flow-types-update/<int:pk>/', FlowTypesUpdate.as_view(), name='flow-types-update'),
    path('creat-flow/', CreatFlow.as_view(), name='creat-flow'),
]
