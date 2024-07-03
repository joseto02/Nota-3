from django.contrib import admin
from django.urls import path, include
from cuenta.views import user_login

urlpatterns = [
    path("admin/", admin.site.urls),
    path("zapatillas/", include("zapatillas.urls")),
    path("login/", user_login, name='login')
]
