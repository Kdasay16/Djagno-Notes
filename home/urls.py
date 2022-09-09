from django.urls import path

from . import views

# we made this file so that we can more dynamically add these routes to smartnotes/url.py
urlpatterns = [
    path('home', views.HomeView.as_view()),
    path('authorized', views.AuthorizedView.as_view())
]
