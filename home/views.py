from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib.auth.decorators import login_required


class HomeView(TemplateView):
    template_name = 'home/welcome.html'
    extra_context = {'today': datetime.today()}

# This has been replaced with the HomeView class to make this a "class based view"
# def home(request):
#     # today is passed into the html file to be used there
#     return render(request, 'home/welcome.html', {'today': datetime.today()})


class AuthorizedView(LoginRequiredMixin, TemplateView):
    template_name = 'home/authorized.html'
    login_url = '/admin'

# This has been replaced with the AuthorizedView class to make this a "class based view"
# login_required tells django the user must be logged in to view the page
# the parameter passed will redirect the user to the login screen
# @login_required(login_url='/admin')
# def authorized(request):
#     return render(request, 'home/authorized.html', {})
