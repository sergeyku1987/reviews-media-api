from django.urls import path

from rest_framework_simplejwt.views import(
    TokenObtainPairView,
    TokenRefreshView,
)

from users.views import RegistrationView, TokenView

urlpatterns = [
    path('token/', TokenView.as_view()),
    path('signup/', RegistrationView.as_view()),
   # path('token/', TokenView.as_view())

]
