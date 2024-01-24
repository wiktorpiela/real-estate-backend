from rest_framework import serializers
from .models import Listing

class ListingSerializer(serializers.ModelSerializer):
    seller = serializers.StringRelatedField()
    seller_agency_name = serializers.SerializerMethodField()

    def get_seller_agency_name(self, obj):
        return obj.seller.profile.agency_name
    
    class Meta:
        model = Listing
        fields = "__all__"