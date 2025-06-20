from rest_framework import serializers
from .models import ArtisanPortfolio, PortfolioImage, Ratings


class PortfolioImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PortfolioImage
        fields = ['id','artisan', 'image', 'description', 'uploaded_at']
        read_only_fields = ['artisan']
        
class RatingSerializer(serializers.ModelSerializer):
    customer = serializers.StringRelatedField(read_only=True)
    # artisan = serializers.StringRelatedField(read_only=True) 
    
    class Meta:
        model = Ratings
        fields = ['id', 'customer','rating', 'comment', 'created_at']
        
class ArtisanPortfolioSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    images = PortfolioImageSerializer(many=True, read_only=True)
    ratings = RatingSerializer(many=True, read_only=True)
    
    class Meta:
        model = ArtisanPortfolio
        fields = ['id', 'user', 'full_name', 'skills', 'location', 'images', 'ratings']
            
        