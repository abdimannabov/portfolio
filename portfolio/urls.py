from django.urls import path
from portfolio.views import *

urlpatterns = [
    path("", index, name="index")
]