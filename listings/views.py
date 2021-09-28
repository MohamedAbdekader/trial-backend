from .serializers import ListingSerializer
from .models import Listing
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import SAFE_METHODS, BasePermission
from rest_framework import generics

class UserPermission(BasePermission):
    message = 'Handling listings is restricted to the creator only.'

    def has_object_permission(self, request, view, obj):

        if request.method in SAFE_METHODS:
            return True
        
        return obj.creator == request.user

class ListingsAll(generics.ListAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

class ListingCreate(generics.CreateAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

class ListingDelete(generics.DestroyAPIView, UserPermission):
    authentication_classes = [TokenAuthentication]
    permission_classes = [UserPermission]
    serializer_class = ListingSerializer
    queryset = Listing.objects.all()

#ListingUpdate
#ListingLookupView

