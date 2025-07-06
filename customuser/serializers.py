from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str
from rest_framework import serializers
from django.core.mail import send_mail




CustomUser = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    
    class Meta:
        model = CustomUser
        fields = ('email', 'password', 'password2', 'phone_number', 'profile_picture', 'address')
        
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password do not match."})
        return attrs
    
    def create(self, validated_data):
        validated_data.pop('password2')
        user = CustomUser.objects.create_user(**validated_data)
        user.is_active = True
        user.save()
        return user
    
class PasswordResetRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()
    
    def validate_email(self, value):
        if not CustomUser.objects.filter(email=value).exists():
            raise serializers.ValidationError("User with this email does not exist.")
        return value
    
    def save(self):
        email = self.validated_data['email']
        user = CustomUser.objects.get(email=email)
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        token = PasswordResetTokenGenerator().make_token(user)
        
        reset_link = f"http://localhost:8000/api/customuser/password-reset/?uid={uid}&token={token}"
        
        send_mail(
            subject="Password Reset",
            message=f"Reset your password using this link: {reset_link}",
            from_email=None,
            recipient_list=[user.email],
        )
        return user
        
class PasswordResetConfirmSerializer(serializers.Serializer):
    uid = serializers.CharField()
    token = serializers.CharField()
    new_password = serializers.CharField(write_only=True, min_length=8)
    
    def validate(self, attrs):
        try:
            uid = force_str(urlsafe_base64_decode(attrs['uid']))
            self.user = CustomUser.objects.get(pk=uid)
        except Exception:
            raise serializers.ValidationError({"uid"})
        
        if not PasswordResetTokenGenerator().check_token(self.user, attrs['token']):
            raise serializers.ValidationError({"token": "Invalid or expired token"})
        
        return attrs
    
    def save(self):
        self.user.set_password(self.validated_data['new_password'])
        self.user.save()
        return self.user
    
