from django.urls import path
from .views import GoogleLogin, FacebookLogin, TwitterLogin

urlpatterns = [
    path('auth/social/google/', GoogleLogin.as_view(), name='google-login'),
    path('auth/social/facebook/', FacebookLogin.as_view(), name='facebook-login'),
    path('auth/social/twitter/', TwitterLogin.as_view(), name='twitter-login'),
]
