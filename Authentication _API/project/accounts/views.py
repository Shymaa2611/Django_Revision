from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer
from django.contrib.auth import logout
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.models import User
from django.core.mail import send_mail
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
#from rest_framework_simplejwt.tokens import RefreshToken
from oauth2_provider.models import AccessToken, RefreshToken


#=========================== Session Authentication ========================

""" class SignupView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"detail": "User created successfully."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        form = AuthenticationForm(data=request.data)
        if form.is_valid():
            user = form.get_user()
            login(request, user) 
            return Response({"detail": "Login successful."}, status=status.HTTP_200_OK)
        return Response({"detail": "Invalid credentials."}, status=status.HTTP_400_BAD_REQUEST)

class LogoutView(APIView):
    def post(self, request):
        logout(request)  
        return Response({"detail": "Logout successful."}, status=200)
    
class PasswordResetView(APIView):
    def post(self, request):
        email = request.data.get('email')
        try:
            user = User.objects.get(email=email)
            token = default_token_generator.make_token(user)
            reset_link = f'http://127.0.0.1/reset-password/{token}/?user_id={user.id}' 
            send_mail(
                'Password Reset',
                f'Click on the following link to reset your password: {reset_link}',
                'app.com',
                [email]
            )
            return Response({'detail': 'Password reset link sent to email.'}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'detail': 'Email address not found.'}, status=status.HTTP_400_BAD_REQUEST)
         
class CompleteResetPassword(APIView):
    def post(self, request,token,pk):
        new_password = request.data.get('new_password')

        if not new_password:
            return Response({"detail": "New password is required."}, status=status.HTTP_400_BAD_REQUEST)
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response({"detail": "Invalid user or token."}, status=status.HTTP_400_BAD_REQUEST)
        if not default_token_generator.check_token(user, token):
            return Response({"detail": "Invalid or expired token."}, status=status.HTTP_400_BAD_REQUEST)
        user.set_password(new_password)
        user.save()

        return Response({"detail": "Password reset successful."}, status=status.HTTP_200_OK)
 
 """
#=========================== TokenAuthentication ========================


""" 
class SignupView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = Token.objects.create(user=user)
            return Response({"token": token.key, "detail": "User created successfully."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        token = Token.objects.get(user=request.user)
        token.delete()
        return Response({"detail": "Logout successful."}, status=200)

class PasswordResetView(APIView):
    def post(self, request):
        email = request.data.get('email')
        try:
            user = User.objects.get(email=email)
            token = default_token_generator.make_token(user)
            reset_link = f'http://localhost:8000/reset-password/{token}/?user_id={user.id}'  
            send_mail(
                'Password Reset',
                f'Click on the following link to reset your password: {reset_link}',
                'app.com',
                [email]
            )
            return Response({'detail': 'Password reset link sent to email.'}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'detail': 'Email address not found.'}, status=status.HTTP_400_BAD_REQUEST)

class CompleteResetPassword(APIView):
    def post(self, request,token,pk):
        new_password = request.data.get('new_password')

        if not new_password:
            return Response({"detail": "New password is required."}, status=status.HTTP_400_BAD_REQUEST)
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response({"detail": "Invalid user or token."}, status=status.HTTP_400_BAD_REQUEST)
        if not default_token_generator.check_token(user, token):
            return Response({"detail": "Invalid or expired token."}, status=status.HTTP_400_BAD_REQUEST)
        user.set_password(new_password)
        user.save()

        return Response({"detail": "Password reset successful."}, status=status.HTTP_200_OK)
 
 """
#=========================== JWTAuthentication ========================


""" class SignupView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"detail": "User created successfully."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data.get('refresh_token')
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"detail": "Logout successful."}, status=200)
        except Exception as e:
            return Response({"detail": str(e)}, status=400)

class PasswordResetView(APIView):
    def post(self, request):
        email = request.data.get('email')
        try:
            user = User.objects.get(email=email)
            token = default_token_generator.make_token(user)
            reset_link = f'http://localhost:8000/reset-password/{token}/?user_id={user.id}'  
            send_mail(
                'Password Reset',
                f'Click on the following link to reset your password: {reset_link}',
                'app.com',
                [email]
            )
            return Response({'detail': 'Password reset link sent to email.'}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'detail': 'Email address not found.'}, status=status.HTTP_400_BAD_REQUEST)

class CompleteResetPassword(APIView):
    def post(self, request,token,pk):
        new_password = request.data.get('new_password')

        if not new_password:
            return Response({"detail": "New password is required."}, status=status.HTTP_400_BAD_REQUEST)
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response({"detail": "Invalid user or token."}, status=status.HTTP_400_BAD_REQUEST)
        if not default_token_generator.check_token(user, token):
            return Response({"detail": "Invalid or expired token."}, status=status.HTTP_400_BAD_REQUEST)
        user.set_password(new_password)
        user.save()

        return Response({"detail": "Password reset successful."}, status=status.HTTP_200_OK)
  """
# ============================ OAuth2 Authentication ==============================

class SignupView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"detail": "User created successfully."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        try:
            refresh_token = request.data.get('refresh_token')
            token = RefreshToken.objects.get(token=refresh_token)
            token.revoke()
            return Response({"detail": "Logout successful."}, status=200)
        except RefreshToken.DoesNotExist:
            return Response({"detail": "Invalid refresh token."}, status=400)

class PasswordResetView(APIView):
    def post(self, request):
        email = request.data.get('email')
        try:
            user = User.objects.get(email=email)
            token = default_token_generator.make_token(user)
            reset_link = f'http://localhost:8000/reset-password/{token}/?user_id={user.id}'  
            send_mail(
                'Password Reset',
                f'Click on the following link to reset your password: {reset_link}',
                'app.com',
                [email]
            )
            return Response({'detail': 'Password reset link sent to email.'}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'detail': 'Email address not found.'}, status=status.HTTP_400_BAD_REQUEST)

class CompleteResetPassword(APIView):
    def post(self, request,token,pk):
        new_password = request.data.get('new_password')

        if not new_password:
            return Response({"detail": "New password is required."}, status=status.HTTP_400_BAD_REQUEST)
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response({"detail": "Invalid user or token."}, status=status.HTTP_400_BAD_REQUEST)
        if not default_token_generator.check_token(user, token):
            return Response({"detail": "Invalid or expired token."}, status=status.HTTP_400_BAD_REQUEST)
        user.set_password(new_password)
        user.save()

        return Response({"detail": "Password reset successful."}, status=status.HTTP_200_OK)
 