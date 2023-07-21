from django.urls import path
from .views import index, top_sellers

urlpatterns = [
    path('index.html', index, name='main-page'),
    path('top-sellers.html', top_sellers, name='top-sellers')
]