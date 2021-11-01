from .serializers import ListingSerializer, ListingLikeCountSerializer
from .models import Listing, ListingLikeCount
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import SAFE_METHODS, BasePermission, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics

class CreatorPermission(BasePermission):
    message = 'Handling listings is restricted to the creator only.'

    def has_object_permission(self, request, view, obj):

        if request.method in SAFE_METHODS:
            return True
        
        return obj.creator == request.user

class ListingsAll(generics.ListAPIView):
    serializer_class = ListingSerializer
    queryset = Listing.objects.all()

# class ListingCreate(generics.CreateAPIView):
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [IsAuthenticated]
#     serializer_class = ListingSerializer
#     queryset = Listing.objects.all()
#     parser_classes = [MultiPartParser, FormParser]

class ListingCreate(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, format=None):
            print(request.data)
            serializer = ListingSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Lookup field on object is default:pk
class ListingDelete(generics.DestroyAPIView, CreatorPermission):
    authentication_classes = [TokenAuthentication]
    permission_classes = [CreatorPermission]
    serializer_class = ListingSerializer
    queryset = Listing.objects.all()

class ListingUpdate(generics.UpdateAPIView, CreatorPermission):
    parser_classes = [FormParser, MultiPartParser]
    authentication_classes = [TokenAuthentication]
    permission_classes = [CreatorPermission]
    serializer_class = ListingSerializer
    queryset = Listing.objects.all()

class ListingLike(generics.UpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ListingLikeCountSerializer
    queryset = ListingLikeCount.objects.all()

class ListingLookup(generics.RetrieveAPIView):
    serializer_class = ListingSerializer
    queryset = Listing.objects.all()

class ListingLikeLookup(generics.RetrieveAPIView):
    serializer_class = ListingLikeCountSerializer
    queryset = ListingLikeCount.objects.all()