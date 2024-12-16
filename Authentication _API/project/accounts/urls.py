from django.urls import path
from .views import *
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from oauth2_provider.views import TokenView

urlpatterns = [
    #=================== SessionAuthentication ==============================#
    #  path('signup/', SignupView.as_view(), name='signup'),
    #  path('login/', LoginView.as_view(), name='login'),
    #  path('logout/', LogoutView.as_view(), name='logout'),
    #  path('password-reset/', PasswordResetView.as_view(), name='password_reset'),
    #  path('complete-reset/<str:token>/<int:pk>/', CompleteResetPassword.as_view(), name='complete_reset'),
    
    #=================== TokenAuthentication ==============================#
    
    # path('signup/', SignupView.as_view(), name='signup'),
    # path('login/', obtain_auth_token, name='api_token_auth'),
    # path('logout/', LogoutView.as_view(), name='logout'),
    # path('password-reset/', PasswordResetView.as_view(), name='password_reset'),
    #  path('complete-reset/<str:token>/<int:pk>/', CompleteResetPassword.as_view(), name='complete_reset'),
   
    #=================== JWTAuthentication ==============================# 
   
    # path('signup/', SignupView.as_view(), name='signup'),
    # path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('logout/', LogoutView.as_view(), name='logout'),
    # path('password-reset/', PasswordResetView.as_view(), name='password_reset'),
    #  path('complete-reset/<str:token>/<int:pk>/', CompleteResetPassword.as_view(), name='complete_reset'),
    
    #=================== OAuth2 Authentication ==============================# 
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', TokenView.as_view(), name='token'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password-reset/', PasswordResetView.as_view(), name='password_reset'),
    path('complete-reset/<str:token>/<int:pk>/', CompleteResetPassword.as_view(), name='complete_reset'),
   
]

