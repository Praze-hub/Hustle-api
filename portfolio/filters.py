from django_filters import rest_framework as filters
from .models import ArtisanPortfolio

class ArtisanPortfolioFilter(filters.FilterSet):
    skills = filters.CharFilter(lookup_expr='icontains')
    location = filters.CharFilter(lookup_expr='icontains')
    min_rating = filters.NumberFilter(method='filter_by_rating')
    
    class Meta:
        model = ArtisanPortfolio
        fields = ['skills', 'location']
        
    def filter_by_rating(self, queryset, name, value):
        return queryset.annotate_avg_rating().filter(avg_rating__gte=value)
    
    