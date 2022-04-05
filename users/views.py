from django.shortcuts import render
from django.http.response import JsonResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from . import services
from .models import User


class UserListView(ListView):
    services.create_user()
    template_name = "users/user_list.html"
    context_object_name = "latest_user_list"
    
    def get_queryset(self):
        return User.objects.order_by('-age')[:10]


class UserDetailView(DetailView):
    model = User
    template_name = "users/user_detail.html"
