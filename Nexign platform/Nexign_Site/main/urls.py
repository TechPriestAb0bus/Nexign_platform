from django.contrib import admin
from django.urls import path
from . import views
from .views import LoginView, RegistrationView

urlpatterns = [
    path('', views.start),
    path('Start', views.start),
    path('Login', LoginView.as_view(), name='login'),
    path('Registration', RegistrationView.as_view(), name='registration'),
    path('admin', admin.site.urls),
    path('About', views.about),
    path('Courses', views.courses),
    path('Elements', views.elements),
    path('News', views.news),
    path('Teachers', views.teachers),
    path('Contact', views.contact),
    path('Platform', views.index)
]
