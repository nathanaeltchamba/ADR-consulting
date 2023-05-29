from django.urls import path
from .views import Homepage, About

# routes
urlpatterns = [
    path('', Homepage.as_view(), name = 'home'),
    path('about/', About.as_view(), name = 'about'),
]