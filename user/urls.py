from django.urls import path
from . import views

urlpatterns = [
  path("postSign/", views.postSign),
  path("register/", views.register),
  path("forgotPassword/", views.forgotPassword)
]
