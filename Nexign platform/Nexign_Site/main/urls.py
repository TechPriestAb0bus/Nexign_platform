from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views
from .views import LoginView, RegistrationView

urlpatterns = [
    path('', views.start),
    path('calendar.php', views.calendar),
    path('exercises.php', views.exercises),
    path('feedback.php', views.feedback),
    path('hackathon.php', views.hackathon),
    path('index.html', views.index),
    path('Lessons-Ansible.php', views.Lessons_Ansible),
    path('Lessons-Atlassian-Bamboo.php', views.Lessons_Atlassian),
    path('Lessons-Common-Installer.php', views.Lessons_Common),
    path('Lessons-Confluence.php', views.Lessons_Confluence),
    path('Lessons-Docker.php', views.Lessons_Docker),
    path('Lessons-Gitlab-CI.php', views.Lessons_GitlabCI),
    path('Lessons-Jira.php', views.Lessons_Jira),
    path('Lessons-Kubernetes.php', views.Lessons_Kubernetes),
    path('meet_up.php', views.meet_up),
    path('provided_material.php', views.provided_material),
    path('video.php', views.video),
    path('logout', LogoutView.as_view(next_page='/'), name='logout'),
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
