from django.urls import path, include
# from .views import CustomRegisterView
from . import views
from dj_rest_auth.registration.views import VerifyEmailView
from rest_framework.permissions import AllowAny
from dj_rest_auth.registration.views import RegisterView
from .views import delete_user

urlpatterns = [
    # path('signup/', CustomRegisterView.as_view(), name='custom_signup'),
    path('', include('dj_rest_auth.urls')),
    path('registration/', include('dj_rest_auth.registration.urls')),
    path('registration/account-confirm-email/', VerifyEmailView.as_view()),
    path('singup/', RegisterView.as_view(), name='rest_register'),
    path('delete-user/', delete_user, name='delete-user'),
    
]