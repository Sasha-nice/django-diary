from django.urls import path
from users.views import UsersViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('api', UsersViewSet, basename='users')

urlpatterns = [

]
urlpatterns += router.urls
