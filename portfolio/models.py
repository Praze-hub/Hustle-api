from django.db import models
from customuser.models import CustomUser

class ArtisanPortfolio(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='artisan_portfolio')
    full_name = models.CharField(max_length=100)
    skills = models.TextField(help_text="skills e.g.,  tailoring, haircut")
    location = models.CharField(max_length=100)
    
    def __str__(self):
        return self.full_name
    
def upload_to(instance, filename):
    return f'artisan_portfolios/{instance.artisan.user.id}/{filename}'

class PortfolioImage(models.Model):
    artisan = models.ForeignKey(ArtisanPortfolio, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to=upload_to)
    description = models.CharField(max_length=255, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    
class Ratings(models.Model):
    artisan = models.ForeignKey(ArtisanPortfolio, on_delete=models.CASCADE, related_name='reviews')
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField()
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('customer', 'artisan') #Prevents duplicates at DB level
    
    
