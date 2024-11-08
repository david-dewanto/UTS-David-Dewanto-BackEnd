from django.urls import path
from ..sample import views

urlpatterns = [
  path("helloworld/", views.say_hello)
]
