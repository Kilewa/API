from django.urls import path
from knox import views as knox_views
from .views import RegisterAPI,LoginAPI, UserApi,UserDetailApi,ProfileApi,ProfileDetailApi


urlpatterns = [
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('api/user', UserApi.as_view()),
    path('api/user/<int:pk>', UserDetailApi.as_view()),
    path('api/profile', ProfileApi.as_view()),
    path('api/profile/<int:pk>', ProfileDetailApi.as_view()),
]
