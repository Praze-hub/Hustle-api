
from rest_framework import viewsets, permissions
from rest_framework.parsers import MultiPartParser, FormParser
from .models import ArtisanPortfolio, PortfolioImage, Ratings
from .serializers import ArtisanPortfolioSerializer, PortfolioImageSerializer, RatingSerializer
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Avg
from .filters import ArtisanPortfolioFilter




class ArtisanPortfolioViewSet(viewsets.ModelViewSet):
    queryset = ArtisanPortfolio.objects.all()
    serializer_class = ArtisanPortfolioSerializer
    permission_classes = [IsAuthenticated]
    filterset_class = ArtisanPortfolioFilter
    search_fields = ['skills', 'location']
    
    def get_queryset(self):
        return ArtisanPortfolio.objects.annotate(
            avg_rating=Avg('reviews__rating')
        )
    
    
    @action(
        detail = False,
        methods = ['post'],
        permission_classes = [IsAuthenticated],
        url_path= "create-portfolio",
        
    )
    def create_portfolio(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
class PortfolioImageViewSet(viewsets.ModelViewSet):
    queryset = PortfolioImage.objects.all()
    serializer_class = PortfolioImageSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]
    
    @action(
        detail=False,
        methods = ['post'],
        permission_classes = [IsAuthenticated],
        parser_classes = [MultiPartParser, FormParser],
        url_path = 'upload-image',
        
    )
    
    def upload_image(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        artisan = request.user.artisan_portfolio
        serializer.save(artisan=artisan)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
class RatingViewSet(viewsets.ModelViewSet):
    queryset = Ratings.objects.all()
    serializer_class = RatingSerializer
    
    def get_queryset(self):
        """
        Optionally restricts the returned ratings to a given artisan,
        by filtering against a 'artisan' query parameter in the URL.
        """
        
        queryset = Ratings.objects.all()
        artisan_id = self.request.query_params.get('artisan')
        if artisan_id is not None:
            queryset = queryset.filter(artisan__id = artisan_id)
        return queryset
    
    @action(
        detail = False,
        methods = ['post'],
        permission_classes = [IsAuthenticated],
        url_path='ratings',
    )
    
    def submit_rating(self, request):
        artisan_id = request.data.get('artisan')
        if not artisan_id:
            raise ValidationError({'artisan': 'This field is required.'})
        
        try:
            artisan = ArtisanPortfolio.objects.get(id=artisan_id)
        except ArtisanPortfolio.DoesNotExist:
            raise ValidationError({'artisan': 'Invalid artisan ID'})
        
        #Enforce uniqueness
        if Ratings.objects.filter(artisan=artisan, customer=request.user).exists():
            raise ValidationError({'detail': 'You have already rated this artisan'})
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(customer=request.user, artisan=artisan)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
        