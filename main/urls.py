
from django.contrib import admin
from django.urls import path, include
from .views import real_home
from rest_framework.authtoken import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', real_home),
    path("api/", include("blog.urls")),
    path("user/", include("user.urls")),
    # path("user/login/",  views.obtain_auth_token),
]
