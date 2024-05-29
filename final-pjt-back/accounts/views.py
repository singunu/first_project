from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth import get_user_model

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import UserRateThrottle
from rest_framework.views import APIView
from dj_rest_auth.registration.views import CreateAPIView

# from .serializers import RegisterSerializer
from dj_rest_auth.registration.serializers import RegisterSerializer

from .models import TokenModel
from .forms import SignUpForm
# from .serializers import

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('main_page')  # 회원가입 후 리다이렉트할 페이지
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

def register_permission_classes():
    return [IsAuthenticated]

User = get_user_model()

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_user(request):
    user = request.user
    user.delete()
    return Response(status=204)

class RegisterView(CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = register_permission_classes()
    token_model = TokenModel
    throttle_scope = 'dj_rest_auth'
    # throttle_classes = [UserRateThrottle]
