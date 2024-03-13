from django.urls import include, path

from rest_framework.routers import DefaultRouter

from api.views import CategoryViewSet, GenreViewSet
from users.views import UserViewSet

router_v1 = DefaultRouter()

router_v1.register(r'categories', CategoryViewSet, basename='category')
router_v1.register(r'genres', GenreViewSet, basename='genre')
router_v1.register(r'users', UserViewSet, basename='user')


urlpatterns = [
    path(r'v1/auth/', include('users.urls')),
    path(r'v1/', include(router_v1.urls)),
    #path(r'v1/users/me/', UserViewSet.as_view())

]

