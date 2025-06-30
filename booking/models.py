from django.db import models
from customuser.models import CustomUser
from portfolio.models import ArtisanPortfolio
from .enums import BookingStatus

class Booking(models.Model):
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='bookings')
    artisan = models.ForeignKey(ArtisanPortfolio, on_delete=models.CASCADE, related_name='bookings')
    service_description = models.TextField()
    service_date = models.DateTimeField()
    location = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=BookingStatus.choices(), default=BookingStatus.PENDING.value)
    
    def __str__(self):
        return f"Booking by {self.customer.email} with {self.artisan.full_name}"
    
    def pending(self):
        self.status = BookingStatus.PENDING.value
        self.save()
        
    def accept(self):
        self.status = BookingStatus.ACCEPTED.value
        self.save()
        
    def decline(self):
        self.status = BookingStatus.DECLINED.value
        self.save()

