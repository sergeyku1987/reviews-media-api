from rest_framework.viewsets import ModelViewSet

from reviews.models import Category, Genre
from api.serializers import CategorySerializer, GenreSerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category
    serializer_class = CategorySerializer


class GenreViewSet(ModelViewSet):
    queryset = Genre
    serializer_class = GenreSerializer
