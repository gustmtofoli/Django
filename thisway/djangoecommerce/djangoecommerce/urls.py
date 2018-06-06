from django.contrib import admin
from django.urls import path, re_path

from core.views import index

urlpatterns = [
    re_path(r'^$', index),
    path('admin/', admin.site.urls),
]
