from django.urls import path

from .views import *


urlpatterns = [
        path("test",    TestView.as_view(), name="test"),
        path("caption", Caption.as_view(), name="caption"),
]