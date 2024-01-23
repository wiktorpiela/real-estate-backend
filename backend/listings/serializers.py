from rest_framework import serializers
from .models import Listing

class ListingSerializer(serializers.ModelSerializer):
    seller = serializers.StringRelatedField()
    
    class Meta:
        model = Listing
        fields = "__all__"