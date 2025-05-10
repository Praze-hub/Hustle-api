from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.google.views import  GoogleOAuth2Adapter
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from allauth.socialaccount.providers.twitter.views import TwitterOAuthAdapter

class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    
class FacebookLogin(SocialLoginView):
    adater_class = FacebookOAuth2Adapter
    
class TwitterLogin(SocialLoginView):
    adapter_class = TwitterOAuthAdapter
    
    