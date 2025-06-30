from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Booking
from .serializers import BookingSerializer
from django.utils.dateparse import parse_date


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        
        #Getting the base queryset for customer OR artisan
        base_queryset = Booking.objects.filter(customer=user) | Booking.objects.filter(artisan__user=user)
        
        #Extract filters from query parameters
        status = self.request.query_params.get('status')
        date_str = self.request.query_params.get('date')
        
        if status:
            base_queryset = base_queryset.filter(status=status)
            
        if date_str:
            date = parse_date(date_str)
            if date:
                base_queryset = base_queryset.filter(date__date=date)
                
        return base_queryset
    
    @action(
        detail=True,
        methods=['post'],
        url_path='accept'
    )
    def accept_booking(self, request, pk=None):
        booking = self.get_object()
        booking.accept()
        return Response({'status': 'Booking Accepted'}, status=status.HTTP_200_OK)
    
    
    @action(
        detail=True,
        methods=['post'],
        url_path='decline'
    )
    def decline_booking(self, request, pk=None):
        booking = self.get_object()
        booking.decline()
        return Response({'status': 'Booking Declined'}, status=status.HTTP_200_OK)
    
    @action(
        detail=True,
        methods=['post'],
        url_path='pending'
    )
    def pending(self, request, pk=None):
        booking = self.get_object()
        booking.pending()
        return Response({'status': 'Booking Pending'}, status=status.HTTP_200_OK)
        

        