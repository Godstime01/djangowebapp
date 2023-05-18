from django.urls import path
from .views import indexView, streamView, uploadView 


urlpatterns = [
    path('', indexView, name='index'),
    path('/stream', streamView, name='stream'),
    path('/upload', uploadView, name='upload'),
    ]