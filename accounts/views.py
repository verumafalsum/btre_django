from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views import View
from django.contrib import messages

class RegisterView(TemplateView):
    template_name = "accounts/register.html"

    def post(self, request):
        messages.error(request, 'Testing error message')
        return redirect('register')


class LoginView(TemplateView):
    template_name = "accounts/login.html"

    def post(self, request):
        
        return redirect('login')

class DashboardView(TemplateView):
    template_name = "accounts/dashboard.html"


def logout(request):
    return redirect('index')
    
