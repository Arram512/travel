from django.contrib import admin
from .models import Tour, ChatHistory


@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    list_display = ['name', 'country', 'tour_type', 'duration_days', 'price', 'rating', 'available']
    list_filter = ['tour_type', 'destination', 'available']
    search_fields = ['name', 'country', 'city', 'description']
    list_editable = ['available']
    ordering = ['-created_at']


@admin.register(ChatHistory)
class ChatHistoryAdmin(admin.ModelAdmin):
    list_display = ['session_id', 'user_message', 'created_at']
    list_filter = ['created_at']
    search_fields = ['session_id', 'user_message', 'ai_response']
    readonly_fields = ['session_id', 'user_message', 'ai_response', 'created_at']
    ordering = ['-created_at']
