from rest_framework import generics, status
from rest_framework.response import Response
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import AccessToken
from django.utils.encoding import smart_str


from .serializers import RegisterSerializer

CustomUser = get_user_model()

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    
    def perform_create(self, serializer):
        user = serializer.save()
        token = RefreshToken.for_user(user).access_token
        current_site = get_current_site(self.request).domain
        relative_link = reverse('verify-email')
        abs_url = f"http://{current_site}{relative_link}?token={str(token)}"
        
        send_mail(
            subject="Verify your email",
            message=f"Click the link to verify your email: {abs_url}",
            from_email = settings.DEFAULT_FROM_EMAIL,
            recipient_list=[user.email]
        )
        
class VerifyEmail(APIView):
    def get(self, request):
        token = request.GET.get('token')
        try:
            access_token = AccessToken(token)
            user_id = access_token['user_id']
            user = CustomUser.objects.get(id=user_id)
            user.is_active = True
            user.save()
            return Response({'message': 'Email verified successfully'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': 'Invalid token or user'}, status=status.HTTP_400_BAD_REQUEST)
        