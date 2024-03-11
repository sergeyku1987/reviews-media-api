from django.urls import include, path

from rest_framework.routers import DefaultRouter

from api.views import CategoryViewSet, GenreViewSet

router_v1 = DefaultRouter()

router_v1.register(r'categories', CategoryViewSet, basename='category')
router_v1.register(r'genres', GenreViewSet, basename='genre')
# router_v1.register(r'auth/signup'       r'auth/token' AuthViewSet

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/auth/', include('users.urls')),
]
