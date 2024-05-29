from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from .models import User
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from allauth.account import app_settings as allauth_account_settings
from django.core.exceptions import ValidationError as DjangoValidationError
from django.contrib.auth import get_user_model
from allauth.account.models import EmailAddress
from dj_rest_auth.serializers import UserDetailsSerializer, PasswordChangeSerializer, PasswordResetConfirmSerializer, PasswordResetSerializer

# class RegisterSerializer(serializers.Serializer):
#     username = serializers.CharField(
#         # max_length=allauth_account_settings.USERNAME_MAX_LENGTH,
#         min_length=allauth_account_settings.USERNAME_MIN_LENGTH,
#         required=allauth_account_settings.USERNAME_REQUIRED,
#     )
#     email = serializers.EmailField(required=allauth_account_settings.EMAIL_REQUIRED)
#     password1 = serializers.CharField(write_only=True)
#     password2 = serializers.CharField(write_only=True)

#     def validate_username(self, username):
#         username = get_adapter().clean_username(username)
#         return username
    
#     def validate_email(self, email):
#         email = get_adapter().clean_email(email)
#         if allauth_account_settings.UNIQUE_EMAIL:
#             if email and EmailAddress.objects.is_verified(email):
#                 raise serializers.ValidationError(
#                     _('A user is alread registered with this e-mail address.'),
#                 )
#         return email

#     def validate_password1(self, password):
#         return get_adapter().clean_password(password)
    
#     def validate(self, data):
#         if data['password1'] != data['password2']:
#             raise serializers.ValidationError(_("The two password fields didn't match."))
#         return data
    
#     def custom_signup(self, request, user):
#         pass

#     def get_cleaned_data(self):
#         return{
#             'username' : self.validated_data.get('username', ''),
#             'password1' : self.validated_data.get('password1', ''),
#             'email' : self.validated_data.get('email', ''),
#         }
    
#     def save(self, request):
#         adapter = get_adapter()
#         user = adapter.new_user(request)
#         self.cleaned_data = self.get_cleaned_data()
#         user = adapter.save_user(request, user, self, commit=False)
#         if "password1" in self.cleaned_data:
#             try:
#                 adapter.clean_password(self.cleaned_data['password1'], user=user)
#             except DjangoValidationError as exc:
#                 raise serializers.ValidationError(
#                     detail=serializers.as_serializer_error(exc)
#                 )
#         user.save()
#         self.custom_signup(request, user)
#         setup_user_email(request, user, [])
#         return user

class CustomRegisterSerializer(RegisterSerializer):
    name = serializers.CharField(required=False)
    birth_date = serializers.DateField(required=False)
    gender = serializers.CharField(required=False)

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data.update({
            'name' : self.validated_data.get('name', None),
            'birth_date': self.validated_data.get('birth_date', None),
            'gender': self.validated_data.get('gender', ''),
        })
        return data

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        user = adapter.save_user(request, user, self, commit=False)
        if "password1" in self.cleaned_data:
            try:
                adapter.clean_password(self.cleaned_data['password1'], user=user)
            except DjangoValidationError as exc:
                raise serializers.ValidationError(
                    detail=serializers.as_serializer_error(exc)
                )
        # 사용자 정의 필드 저장
        user.name = self.cleaned_data.get('name')
        user.birth_date = self.cleaned_data.get('birth_date')
        user.gender = self.cleaned_data.get('gender')
        user.save()
        self.custom_signup(request, user)
        setup_user_email(request, user, [])
        return user
    
class CustomUserDetailsSerializer(UserDetailsSerializer):
    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + ('name', 'birth_date', 'gender')

class CustomUserChangePassword(PasswordChangeSerializer):
    pass