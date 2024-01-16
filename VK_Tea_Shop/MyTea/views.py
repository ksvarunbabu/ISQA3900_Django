from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.
def index(request):
  return HttpResponse("Welcome to VK's Tea Shop. Enjoy your Drinks")

class HomePageView(TemplateView):
  template_name = 'home.html'

class WelcomePage(TemplateView):
  template_name = "welcome.html"