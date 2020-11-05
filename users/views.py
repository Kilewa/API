from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer,ProfileSerializer
from django.contrib.auth import login
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from .models import Profile
from django.contrib.auth.models import User


# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })
class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)             

class UserApi(generics.ListAPIView):
    
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailApi(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = User.objects.all()
    serializer_class = UserSerializer        


class ProfileApi(generics.ListAPIView):
    
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileDetailApi(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProfileSerializer
    def get_queryset(self):
        """
        This view should return a list of all the crops
        for the user.
        """
        queryset = Profile.objects.all()
        userid = self.request.query_params.get('userid', None)
        if userid is not None:
            queryset = queryset.filter(user_id=userid)
        return queryset 