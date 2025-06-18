from rest_framework.routers import DefaultRouter
from .views import ArtisanPortfolioViewSet, PortfolioImageViewSet, RatingViewSet

router = DefaultRouter()
router.register(r'create-portfolio', ArtisanPortfolioViewSet, basename='create-portfolio')
router.register(r'upload-image', PortfolioImageViewSet, basename='upload-image')
router.register(r'ratings', RatingViewSet, basename='ratings')

urlpatterns = router.urls