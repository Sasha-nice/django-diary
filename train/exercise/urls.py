from django.urls import path
from exercise.views import ExerciseViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('api', ExerciseViewSet, basename='exercise')

urlpatterns = [
]
urlpatterns += router.urls

