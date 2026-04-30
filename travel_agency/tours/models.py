from django.db import models

class Tour(models.Model):
    DESTINATIONS = [
        ('EU', 'Европа'),
        ('AS', 'Азия'),
        ('AF', 'Африка'),
        ('NA', 'Северная Америка'),
        ('SA', 'Южная Америка'),
        ('OC', 'Океания'),
    ]
    
    TOUR_TYPES = [
        ('beach', 'Пляжный отдых'),
        ('excursion', 'Экскурсионный'),
        ('active', 'Активный туризм'),
        ('wellness', 'Оздоровительный'),
        ('cruise', 'Круиз'),
    ]
    
    name = models.CharField(max_length=200, verbose_name='Название тура')
    destination = models.CharField(max_length=2, choices=DESTINATIONS, verbose_name='Направление')
    country = models.CharField(max_length=100, verbose_name='Страна')
    city = models.CharField(max_length=100, verbose_name='Город')
    tour_type = models.CharField(max_length=20, choices=TOUR_TYPES, verbose_name='Тип тура')
    duration_days = models.IntegerField(verbose_name='Длительность (дней)')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    description = models.TextField(verbose_name='Описание')
    includes = models.TextField(verbose_name='Что включено')
    image_url = models.URLField(blank=True, verbose_name='URL изображения')
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=0, verbose_name='Рейтинг')
    available = models.BooleanField(default=True, verbose_name='Доступен')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Тур'
        verbose_name_plural = 'Туры'
        ordering = ['-created_at']
    
    def __str__(self):
        return self.name


class ChatHistory(models.Model):
    session_id = models.CharField(max_length=100, db_index=True)
    user_message = models.TextField()
    ai_response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'История чата'
        verbose_name_plural = 'История чатов'
        ordering = ['created_at']
    
    def __str__(self):
        return f"Chat {self.session_id} - {self.created_at}"
