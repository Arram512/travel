from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TourViewSet, chat_message, chat_history, clear_chat_history

router = DefaultRouter()
router.register(r'tours', TourViewSet, basename='tour')

urlpatterns = [
    path('', include(router.urls)),
    path('chat/', chat_message, name='chat-message'),
    path('chat/history/<str:session_id>/', chat_history, name='chat-history'),
    path('chat/clear/<str:session_id>/', clear_chat_history, name='clear-chat-history'),
]
