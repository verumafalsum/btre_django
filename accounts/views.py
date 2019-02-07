from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views import View
from django.contrib import messages, auth
from django.contrib.auth.models import User

class RegisterView(TemplateView):
    template_name = "accounts/register.html"

    def post(self, request):
        # Get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        success = False

        def register():
            user = User.objects.create_user(
                    username=username,
                    password=password,
                    email=email,
                    first_name=first_name,
                    last_name=last_name
                    )
            user.save()
            messages.success(request, 'You are now registered and can log in')
            nonlocal success
            success = True

        def check_username():
            if User.objects.filter(username=username).exists():
                messages.error(request, 'That username is taken')
                return redirect('register')
            else:
                check_email()

        def check_email():
            if User.objects.filter(email=email).exists():
                messages.error(request, 'That email is being used')
                return redirect('register')
            else:
                register()


        if password == password2:
            check_username()
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
        
        if success:
            return redirect('login')
        else:
            messages.error(request, 'Something went wrong')
            return redirect('register')


class LoginView(TemplateView):
    template_name = "accounts/login.html"

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')

class DashboardView(TemplateView):
    template_name = "accounts/dashboard.html"


class LogoutView(View):
    def post(self, request):
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('index')

    
