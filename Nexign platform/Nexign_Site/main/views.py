from django.shortcuts import render
from django import views
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect

from .forms import LoginForm, RegistrationForm
from .models import Developer


def start(request):
    return render(request, 'main/start.html')


def about(request):
    return render(request, 'main/')


def courses(request):
    return render(request, 'main/courses.html')


def elements(request):
    return render(request, 'main/elements.html')

def news(request):
    return render(request, 'main/news.html')


def contact(request):
    return render(request, 'main/contact.html')


def teachers(request):
    return render(request, 'main/teachers.html')


def index(request):
    return render(request, 'main/index.html')


class LoginView(views.View):
    def get(self, request, *args, **kwargs):
        form = LoginForm(request.POST or None)
        context = {
            'form': form
        }
        return render(request, 'main/login.html', context)

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return HttpResponseRedirect('Platform')
        context = {
            'form': form
        }
        return render(request, 'main/login.html', context)


class RegistrationView(views.View):
    def get(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST or None)
        context = {
            'form': form
        }
        return render(request, 'main/registration.html', context)

    def post(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST or None)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.username = form.cleaned_data['username']
            new_user.email = form.cleaned_data['email']
            new_user.first_name = form.cleaned_data['first_name']
            new_user.last_name = form.cleaned_data['last_name']
            new_user.save()
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            Developer.objects.create(
                user=new_user
            )
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            login(request, user)
            return HttpResponseRedirect('Login')
        context = {
            'form': form
        }
        return render(request, 'main/registration.html', context)
