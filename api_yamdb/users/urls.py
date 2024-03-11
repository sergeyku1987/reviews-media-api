from django.urls import path

from rest_framework_simplejwt.views import(
    TokenObtainPairView,
    TokenRefreshView,
)

from users.views import Proxy, MyTokenView

urlpatterns = [
    #path('give-code/', Proxy.as_view()),
    #path('give-token-through-email/', Proxy.as_view()),
    #path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/', MyTokenView.as_view()),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
]
