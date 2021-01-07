from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseForbidden
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from .forms import HomeForm
from django.contrib.auth.models import User


class MainView(View):
    template_name = 'menu/main.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = 'login'
    template_name = 'menu/signup.html'


class MyLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'menu/login.html'


class HomeView(View):
    template_name = 'menu/home.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
