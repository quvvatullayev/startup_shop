from django.urls import path, include
from .views.startupview import StartupViews, StartupView
from .views.userview import StartupUsers, StartupUser
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('startupviews/', StartupViews.as_view()),
    path('startupview/', StartupView.as_view()),
    path('startupusers/', StartupUsers.as_view()),
    path('startupuser/', StartupUser.as_view()),
]