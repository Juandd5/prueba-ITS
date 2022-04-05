from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import JsonResponse

from . import services
from .models import User


def list_users(request):
    services.create_user()
    user_list = list(User.objects.values())

    if user_list:
        data = {
            'Users': user_list
        }
        return JsonResponse(data, status=200)
    return HttpResponse('Not found', status=404)
