import requests
import json
from django.conf import settings
from .models import Tour

class QwenService:
    def __init__(self):
        self.api_url = settings.QWEN_API_URL
        self.api_key = settings.QWEN_API_KEY
        
    def get_system_prompt(self, tours_context):
        return f"""Ты - виртуальный помощник туристической компании "Мир Путешествий". 
Твоя задача - помочь клиенту выбрать идеальный тур.

Доступные туры в базе данных:
{tours_context}

Правила общения:
1. Будь дружелюбным и вежливым
2. Задавай уточняющие вопросы о предпочтениях клиента (бюджет, направление, тип отдыха, длительность)
3. Рекомендуй туры на основе предпочтений клиента
4. Если клиент спрашивает про конкретный тур, предоставь детальную информацию
5. Если подходящих туров нет, предложи альтернативы
6. Отвечай на русском языке кратко и по делу

Формат рекомендаций:
- Название тура
- Краткое описание
- Цена
- Длительность"""

    def get_tours_context(self):
        tours = Tour.objects.filter(available=True)[:20]
        context = []
        for tour in tours:
            context.append(
                f"- {tour.name}: {tour.country}, {tour.city}. "
                f"Тип: {tour.get_tour_type_display()}. "
                f"Длительность: {tour.duration_days} дней. "
                f"Цена: {tour.price} руб. "
                f"Описание: {tour.description[:100]}..."
            )
        return "\n".join(context)

    def chat(self, user_message, conversation_history=None):
        """
        Send message to Qwen model and get response
        """
        if conversation_history is None:
            conversation_history = []
        
        tours_context = self.get_tours_context()
        system_prompt = self.get_system_prompt(tours_context)
        
        messages = [
            {"role": "system", "content": system_prompt}
        ]
        
        # Add conversation history
        messages.extend(conversation_history)
        
        # Add current user message
        messages.append({"role": "user", "content": user_message})
        
        try:
            # Call Qwen API (compatible with OpenAI format)
            headers = {
                "Content-Type": "application/json",
            }
            
            if self.api_key:
                headers["Authorization"] = f"Bearer {self.api_key}"
            
            payload = {
                "model": "qwen",  # или конкретная модель, например "Qwen2.5-7B-Instruct"
                "messages": messages,
                "temperature": 0.7,
                "max_tokens": 500,
            }
            
            response = requests.post(
                self.api_url,
                headers=headers,
                json=payload,
                timeout=30
            )
            
            if response.status_code == 200:
                result = response.json()
                ai_response = result['choices'][0]['message']['content']
                return ai_response
            else:
                return "Извините, произошла ошибка при обработке вашего запроса. Пожалуйста, попробуйте позже."
                
        except requests.exceptions.RequestException as e:
            print(f"Error calling Qwen API: {e}")
            return "Извините, сервис временно недоступен. Пожалуйста, попробуйте позже."
    
    def extract_tour_recommendations(self, user_message, ai_response):
        """
        Extract relevant tours based on conversation context
        """
        # Simple keyword matching for tour recommendations
        keywords = user_message.lower().split()
        
        tours = Tour.objects.filter(available=True)
        
        # Filter by keywords
        for keyword in keywords:
            if keyword in ['пляж', 'море', 'пляжный']:
                tours = tours.filter(tour_type='beach')
            elif keyword in ['экскурсия', 'экскурсионный', 'достопримечательности']:
                tours = tours.filter(tour_type='excursion')
            elif keyword in ['активный', 'горы', 'поход']:
                tours = tours.filter(tour_type='active')
            elif keyword in ['оздоровительный', 'спа', 'здоровье']:
                tours = tours.filter(tour_type='wellness')
            elif keyword in ['круиз', 'корабль']:
                tours = tours.filter(tour_type='cruise')
        
        # Return top 3 matching tours
        return tours[:3]
