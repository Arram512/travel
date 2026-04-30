from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Tour, ChatHistory
from .serializers import (
    TourSerializer, 
    ChatMessageSerializer, 
    ChatResponseSerializer,
    ChatHistorySerializer
)
from .ai_service import QwenService
import uuid


class TourViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tour.objects.filter(available=True)
    serializer_class = TourSerializer
    
    def get_queryset(self):
        queryset = Tour.objects.filter(available=True)
        
        # Filtering
        tour_type = self.request.query_params.get('type', None)
        destination = self.request.query_params.get('destination', None)
        min_price = self.request.query_params.get('min_price', None)
        max_price = self.request.query_params.get('max_price', None)
        
        if tour_type:
            queryset = queryset.filter(tour_type=tour_type)
        if destination:
            queryset = queryset.filter(destination=destination)
        if min_price:
            queryset = queryset.filter(price__gte=min_price)
        if max_price:
            queryset = queryset.filter(price__lte=max_price)
            
        return queryset


@api_view(['POST'])
def chat_message(request):
    """
    Handle chat messages with AI assistant
    """
    serializer = ChatMessageSerializer(data=request.data)
    
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    user_message = serializer.validated_data['message']
    session_id = serializer.validated_data.get('session_id', str(uuid.uuid4()))
    
    # Get conversation history for this session
    history = ChatHistory.objects.filter(session_id=session_id).order_by('created_at')
    conversation_history = []
    
    for chat in history:
        conversation_history.append({"role": "user", "content": chat.user_message})
        conversation_history.append({"role": "assistant", "content": chat.ai_response})
    
    # Get AI response
    qwen_service = QwenService()
    ai_response = qwen_service.chat(user_message, conversation_history)
    
    # Save to history
    ChatHistory.objects.create(
        session_id=session_id,
        user_message=user_message,
        ai_response=ai_response
    )
    
    # Extract tour recommendations
    suggested_tours = qwen_service.extract_tour_recommendations(user_message, ai_response)
    
    response_data = {
        'response': ai_response,
        'session_id': session_id,
        'suggested_tours': TourSerializer(suggested_tours, many=True).data if suggested_tours else []
    }
    
    return Response(response_data, status=status.HTTP_200_OK)


@api_view(['GET'])
def chat_history(request, session_id):
    """
    Get chat history for a session
    """
    history = ChatHistory.objects.filter(session_id=session_id).order_by('created_at')
    serializer = ChatHistorySerializer(history, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['DELETE'])
def clear_chat_history(request, session_id):
    """
    Clear chat history for a session
    """
    ChatHistory.objects.filter(session_id=session_id).delete()
    return Response({'message': 'История чата очищена'}, status=status.HTTP_200_OK)
