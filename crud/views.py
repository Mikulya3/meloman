from rest_framework import mixins
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from crud.models import Film, Category
from crud.serializers import FilmSerializer, CategorySerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly



class FilmApiView(ModelViewSet):
    authentication_classes = []
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['tag', 'genre', 'created_at']
    search_fields = ['tag', 'title']


    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset
class CategoryAPIView(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    authentication_classes = []
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]