from django.urls import path, include
from .views import *

urlpatterns = [
    path('', upload_file, name="file_upload"),
    path('success', upload_file, name="success"),
]
