from django.urls import path
from . import views
from .views import HomePageView

urlpatterns = [
    path("test/", views.index, name="index"),
    path('',HomePageView.as_view(), name='home'),
    path('welcome/',views.WelcomePage.as_view(), name='welcome')
]
