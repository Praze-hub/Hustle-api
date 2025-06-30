from rest_framework import serializers
from .models import Booking

class BookingSerializer(serializers.ModelSerializer):
    customer = serializers.HiddenField(default=serializers.CurrentUserDefault())
    
    class Meta:
        model = Booking
        fields = ['id', 'customer', 'artisan', 'service_description', 'service_date', 'location', 'status']
        read_only_fields = ['status', 'created_at']