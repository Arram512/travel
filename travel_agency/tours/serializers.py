from rest_framework import serializers
from .models import Tour, ChatHistory

class TourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tour
        fields = '__all__'


class ChatMessageSerializer(serializers.Serializer):
    message = serializers.CharField()
    session_id = serializers.CharField(required=False)


class ChatResponseSerializer(serializers.Serializer):
    response = serializers.CharField()
    session_id = serializers.CharField()
    suggested_tours = TourSerializer(many=True, required=False)


class ChatHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatHistory
        fields = ['id', 'user_message', 'ai_response', 'created_at']
