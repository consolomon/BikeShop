from django.urls import path
from .views import *


urlpatterns = [
    path('bikes/', BikeListView.as_view(), name='bikes'),
    path('bikes/<int:pk>/', BikeView.as_view(), name='detail'),
    path('order/<int:pk>/', OrderDetailView.as_view(), name='order')
]
