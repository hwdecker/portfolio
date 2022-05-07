from django.urls import path
from django.views.generic import TemplateView
from .views import ProjectListView, ProjectDetailView
from . import views
import portfolio

urlpatterns = [
    path('', TemplateView.as_view(template_name='portfolio/home.html'), name='portfolio-home'),
    path('projects/', ProjectListView.as_view(), name='portfolio-projects'),
    path('project/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
]