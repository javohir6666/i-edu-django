from django.urls import path
from .views import HomePageView, AboutPageView, ContactPageView
from Page.views import Team, ServiceView, ProjectView
urlpatterns = [
    path("about/", AboutPageView.as_view(), name="about"),
    path("contact/", ContactPageView.as_view(), name="contact"),
    path("team/", Team.as_view(), name="team"),
    path("service/", ServiceView.as_view(), name="service"),
    path("projects/", ProjectView.as_view(), name="project"),
    path("", HomePageView.as_view(), name="home"),
]