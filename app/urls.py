from django.urls import path
from .views import Homepage

# routes
urlpatterns = [
    path('', Homepage.as_view(), name = 'home'),
]