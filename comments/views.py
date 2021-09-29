from django.shortcuts import render
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import SAFE_METHODS, BasePermission, IsAuthenticated
from .models import Comment
from .serializers import CommentSerializer

class UserPermission(BasePermission):
    message = 'Handling listings is restricted to the creator only.'

    def has_object_permission(self, request, view, obj):

        if request.method in SAFE_METHODS:
            return True
        
        return obj.creator == request.user

class CommentsAll(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentCreate(generics.CreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

class CommentDelete(generics.DestroyAPIView, UserPermission):
    authentication_classes = [TokenAuthentication]
    permission_classes = [UserPermission]
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

class CommentUpdate(generics.UpdateAPIView, UserPermission):
    authentication_classes = [TokenAuthentication]
    permission_classes = [UserPermission]
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

# class CommentLookup(generics.RetrieveAPIView):
#     serializer_class = CommentSerializer
#     queryset = Comment.objects.all()
