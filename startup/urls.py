from django.urls import path, include
from .views.startupview import StartupViews, StartupView
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('startupviews/', StartupViews.as_view()),
    path('startupview/', StartupView.as_view())
]