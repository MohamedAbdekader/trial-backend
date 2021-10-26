from rest_framework import generics
from rest_framework.response import Response
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

class CommentLookup(generics.RetrieveAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    #override default config looking up by query_param instead of <pk>
    def get(self, request):
        queryset = self.get_queryset()        
        listing_id = request.query_params['listing_id']
        
        if listing_id is not None:
            queryset = queryset.filter(listing=listing_id)
            return Response(CommentSerializer(queryset, many=True).data)

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