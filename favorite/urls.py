from rest_framework.routers import DefaultRouter
from django.urls import path, include

from favorite.views import CommentAPIView, RatingAPIView, LikeAPIView, FavoriteAPIView

router = DefaultRouter()
router.register('comment', CommentAPIView)
router.register('rating', RatingAPIView, basename='rating')
router.register('like', LikeAPIView, basename='like')
router.register('favorite', FavoriteAPIView)

urlpatterns = [
    path('', include(router.urls))
]