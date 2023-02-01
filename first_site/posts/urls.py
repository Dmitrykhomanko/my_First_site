from django.urls import path
from .views import index, post, group


urlpatterns = [
    path('', index),
    path('post/<id>/', post),
    path('group/<name>/',group),
]
