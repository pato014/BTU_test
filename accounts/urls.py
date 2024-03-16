from django.urls import path
from .views import (
    ResgisterUserView,
    VerifyUserEmailView,
    LoginUserView,
    TestingAuthenticatedReq,
    PasswordResetRequestView,
    PasswordResetConfirm,
    SetNewPasswordView
)
from rest_framework_simplejwt.views import (TokenRefreshView, )

urlpatterns = [
    path('register/', ResgisterUserView.as_view(), name='register'),
    path('verify-email/', VerifyUserEmailView.as_view(), name='verify'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('profile/', TestingAuthenticatedReq.as_view(), name='profile'),
    path('password-reset/', PasswordResetRequestView.as_view(), name='password-reset'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirm.as_view(), name='reset-password-confirm'),
    path('set-new-password/', SetNewPasswordView.as_view(), name='set-new-password')
]
