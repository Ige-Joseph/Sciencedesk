from django.urls import path
from . import views

urlpatterns = [
    path('sciencedesk', views.sciencedesk_agent, name='sciencedesk'),
    path('health', views.health_check, name='health'),
]