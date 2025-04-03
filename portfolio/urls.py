from django.urls import path
from portfolio.views import *

urlpatterns = [
    path("", index, name="index"),
    path("detail/", detail, name="detail")
]