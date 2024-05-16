"""
ViewSets це високорівневий абстрактний клас котрий надає зручний та гнучкий
інтерфейс для створення апі CRUD операцій

from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from myapps.serializers import UserSerializer
from rest_framework import viewsets
from rest_framework.response import Response

class UserViewSet(viewsets.ViewSet):
    '''
    A simple ViewSet for listing or retrieving users.
    '''
    def list(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)


Here how can we build urlpatterns:
path('industries/save/', IndustriesStoreViewSet.as_view({'post': 'create'})),
path('industries/save/<int:pk>/', IndustriesStoreViewSet.as_view({'put': 'update'})),
path('industries/delete/<int:pk>/', IndustriesStoreViewSet.as_view({'delete': 'destroy'})),
path('industries/<int:pk>/', IndustriesStoreViewSet.as_view({'get': 'retrieve'})),


ModelViewSet є частиною Django Rest Framework і забезпечує повну
функціональність для створення, читання, оновлення та видалення об'єктів моделі Django

from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Підключіть ViewSet до шляхів вашого API
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'books', BookViewSet)
urlpatterns = router.urls
"""