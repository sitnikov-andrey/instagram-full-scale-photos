from django.urls import path
from .views import *

urlpatterns = [
    path('', search_page, name = 'search_url'),
    path('get_photo', get_photo, name = 'get_photo_url'),
]