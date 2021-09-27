from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework import serializers, viewsets, permissions, authentication, generics
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from .models import Profile
from .serializers import ProfileSerializer
from rest_framework.response import Response
from rest_framework.permissions import SAFE_METHODS, BasePermission

# class UserPermission(BasePermission):
#     message = 'Editing profiles is restricted to the creator only.'

#     def has_object_permission(self, request, view, obj):

#         if request.method in SAFE_METHODS:
#             return True

#         return obj.user == request.user

# class UserCreate(APIView):
#     permission_classes = [AllowAny]

#     def post(self, request, format='json'):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.save()
#             if user:
#                 json = serializer.data
#                 return Response(json)
#         return Response(serializer.errors)
    
# class UserDelete(APIView):
#     # authentication_classes = [authentication.TokenAuthentication, ]
#     # permission_classes = [UserPermission]

#     def delete(self, request, pk, format=None):
#         user = User.objects.get(username=pk)
#         user.delete()
#         return Response({"message": "User deleted", "username": user.username})

class ProfileView(generics.RetrieveAPIView):

    serializer_class = ProfileSerializer

    def get_object(self, queryset=None, **kwargs):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Profile, user_name=pk)
