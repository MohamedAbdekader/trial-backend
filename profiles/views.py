from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
# from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import Profile
from .serializers import ProfileSerializer
from rest_framework.response import Response
from rest_framework.permissions import SAFE_METHODS, BasePermission

# class ExampleView(APIView):
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [IsAuthenticated]

#     def get(self, request, format=None):
#         content = {
#             'user': str(request.user),  # `django.contrib.auth.User` instance.
#             'auth': str(request.auth),  # None
#         }
#         return Response(content)

class UserPermission(BasePermission):
    message = 'Editing profiles is restricted to the creator only.'

    def has_object_permission(self, request, view, obj):

        if request.method in SAFE_METHODS:
            return True
        #obj default pk is 'username' => from def '__str__'
        return obj == request.user

class ProfileList(generics.ListAPIView):
    # permission_classes = [IsAdminUser]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ProfileCreate(APIView):
    permission_classes = [AllowAny]

    def post(self, request, format='json'):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json)
        return Response(serializer.errors)
    
class ProfileDelete(generics.DestroyAPIView, UserPermission):
    authentication_classes = [TokenAuthentication]
    permission_classes = [UserPermission]
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

class ProfileUpdate(generics.UpdateAPIView, UserPermission):
    authentication_classes = [TokenAuthentication]
    permission_classes = [UserPermission]
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()    

class ProfileView(generics.RetrieveAPIView):
    serializer_class = ProfileSerializer

    def get_object(self, queryset=None, **kwargs):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Profile, username=pk)
