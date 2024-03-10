from django.shortcuts import render, HttpResponse
from requests import Response

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated

from users.models import CustomUser
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

import jwt
import json


from drfTuron.settings import SECRET_KEY


# Create your views here.

@method_decorator(csrf_exempt, name='dispatch')
def login(request):
    try:
        data = json.loads(request.body)
        token = data.get('token')
        decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        user_id = decoded.get("user_id")
        user = CustomUser.objects.get(pk=user_id)
        print(user)
    except jwt.ExpiredSignatureError:
        print('yaroqli muddati otgan')
    return render(request, 'users/login/login.html')


class Logout(APIView):
    def get(self, request, format=None):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)

