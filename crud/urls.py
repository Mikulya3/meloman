from django.urls import path,include
from rest_framework.routers import DefaultRouter
from crud.views import FilmApiView, CategoryAPIView

router =DefaultRouter()
router.register('category', CategoryAPIView)
router.register('', FilmApiView)


urlpatterns = [
    path('', include(router.urls)),
]