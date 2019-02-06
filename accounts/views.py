from django.shortcuts import render, redirect
from django.views.generic import TemplateView

class RegisterView(TemplateView):
    template_name = "accounts/register.html"


class LoginView(TemplateView):
    template_name = "accounts/login.html"


class DashboardView(TemplateView):
    template_name = "accounts/dashboard.html"


def logout(request):
    return redirect('index')
    
