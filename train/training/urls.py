from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from .views import get_post, get_put_delete, post_form
from training.views import TrainingViewSet
from rest_framework.routers import DefaultRouter
from training.views import search, search1, centrifugo, post_from_get
router = DefaultRouter()
router.register('api', TrainingViewSet, basename='training')

urlpatterns = [
    path('<int:iid>/', get_put_delete),
    path('', get_post),
    path('centr/', centrifugo),
    path('forms/', post_form),
    path('search/<str:field>/', search),
    path('search/<str:field>/<str:value>/', search1),
    path('tyt/', post_from_get)
]
urlpatterns += router.urls
