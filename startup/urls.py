from django.urls import path, include
from .views.startupview import StartupListCreateViews
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('startuplistcreate/', StartupListCreateViews.as_view())
]