from django.urls import path 

from .views import tour_detail

urlpatterns = [
    path('<int:pk>/', tour_detail, name='tour_detail'),
]