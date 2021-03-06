from django.urls import path

from . import views

app_name = 'users'
urlpatterns = [
    path('', views.UserListView.as_view(), name='list'),
    path('<int:pk>', views.UserDetailView.as_view(), name='detail'),
]
