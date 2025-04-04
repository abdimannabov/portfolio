from django.urls import path
from portfolio.views import *

urlpatterns = [
    path("", index, name="index"),
    path("detail/<int:pk>/", detail, name="detail")
]