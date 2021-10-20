from rest_framework import serializers
from .models import Listing, ListingLikeCount

class ListingSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Listing
        fields = '__all__'

class ListingLikeCountSerializer(serializers.ModelSerializer):
    class Meta: 
        model = ListingLikeCount
        fields = '__all__'