from django.urls import path
from .views import index_

urlpatterns = [
    path('lesson_4', index_),
]