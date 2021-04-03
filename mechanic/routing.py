from django.urls import path
from .consumers import WSConsumer

ws_urlpatterns = [
    path('ws/mechanic_dashboard_url/', WSConsumer.as_asgi())
]
