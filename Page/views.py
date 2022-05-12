from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView
from Team.models import Worker
from Service.models import ServiceModel
from Project.models import ProjectModel
from .models import PageModel
# Create your views here.


class HomePageView(TemplateView):  # home page
    template_name = "index.html"
class AboutPageView(TemplateView):  # about page
    template_name = "about.html"
class ContactPageView(TemplateView):  # contact page
    template_name = "contact.html"
class PageView(DetailView):
    model = PageModel         # page view
    context_object_name = 'Page'
    template_name = "page.html"
    
class Team(ListView):  # Team page
    model = Worker
    context_object_name = 'Team'
    template_name = 'team.html'
    
class ServiceView(ListView):  # service page
    model = ServiceModel
    context_object_name = 'Service'
    template_name = 'service.html'
    
class ProjectView(ListView):  # Projects page
    model = ProjectModel
    context_object_name = 'Project'
    template_name = 'project.html'