from django.urls import path, include
from rest_framework import routers
from .views import home, BlogMVS, CategoriesMVS

router = routers.DefaultRouter()
router.register("blog", BlogMVS)
router.register("categories", CategoriesMVS)



urlpatterns = [
    #! function views
    path("", home),

    path("", include(router.urls))
]