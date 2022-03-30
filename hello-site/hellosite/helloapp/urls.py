from django.urls import path
from sayhello.views import HelloWorldView

urlpatterns = [
    path('', HellowWorldView.as_view(), name='hello_world'),
    ]