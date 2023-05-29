from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class Homepage(TemplateView):
    template_name = 'homepage.html'

class About(TemplateView):
    template_name = 'about/about.html'