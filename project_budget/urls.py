from django.contrib import admin
from django.urls import path, include
from user_manager.views import BaseView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", BaseView.as_view(), name='base'),
    path("user/", include("user_manager.urls")),
    path("balance/", include("balance.urls")),
]
