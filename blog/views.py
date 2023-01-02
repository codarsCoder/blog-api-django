
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Blog, Category
from .serializers import BlogSerializer, CategorySerializer
from rest_framework.permissions import BasePermission, IsAuthenticated,IsAuthenticatedOrReadOnly,IsAdminUser
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter
@api_view()  # default GET
def home(requst):
    return Response({'home': 'This is home page...'})


class BlogMVS(ModelViewSet):
    
    queryset = Blog.objects.filter(status=1)
    serializer_class = BlogSerializer
    permission_classes=[IsAuthenticated]   # settingste REST_FRAMEWORK kısmına ekleme yapmayı unutma !
    filter_backends=[DjangoFilterBackend,SearchFilter,OrderingFilter]  ##burası local olarak filter_backends eklemek için sırayla filtreleme,search ve ordering ekledik  bura yoksa settings.py den de ekleme yapılmalı
    filterset_fields=['id','title','content'] #filtreleme için alanlar
    search_fields=['title','content'] # search yapılacak alanlar belirlendi
    
    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_superuser: #super user ise hepsini gör is_staff vs de konulabilirdi
            return queryset
        return queryset.filter(user_id=self.request.user.id)  ## tabloda user_id tutyoruz bu yüzden user_id leri filtreledik
    
class CategoriesMVS(ModelViewSet):
    
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes=[IsAdminUser]