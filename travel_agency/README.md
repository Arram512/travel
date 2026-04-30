# Туристическая компания с AI-помощником 🌍✈️

Современный веб-сайт туристической компании с интегрированным AI-ассистентом для подбора туров на основе Qwen (легковесная LLM модель).

## 🎯 Возможности

- **AI-помощник**: Интеллектуальный чат-бот на базе Qwen для подбора туров
- **Каталог туров**: Красивые карточки с фильтрацией
- **Адаптивный дизайн**: Работает на всех устройствах
- **История диалогов**: Сохранение контекста разговора
- **Рекомендации**: Автоматический подбор туров на основе предпочтений

## 🛠 Технологии

**Backend:**
- Django 4.2.8
- Django REST Framework
- SQLite
- Qwen LLM (через OpenAI-совместимый API)

**Frontend:**
- React 18
- CSS3
- Fetch API

## 📁 Структура проекта
```
travel_agency/
├── backend/              # Django settings
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── tours/                # Django app
│   ├── __init__.py
│   ├── models.py         # Tour и ChatHistory модели
│   ├── views.py          # API endpoints
│   ├── serializers.py
│   ├── ai_service.py     # Интеграция с Qwen
│   ├── admin.py
│   ├── urls.py
│   └── management/
│       └── commands/
│           └── populate_tours.py
├── frontend/             # React app
│   ├── public/
│   │   └── index.html
│   ├── src/
│   │   ├── components/
│   │   │   ├── ChatBot.jsx
│   │   │   ├── ChatBot.css
│   │   │   ├── ToursList.jsx
│   │   │   ├── ToursList.css
│   │   │   ├── Header.jsx
│   │   │   ├── Header.css
│   │   │   ├── Hero.jsx
│   │   │   └── Hero.css
│   │   ├── App.jsx
│   │   ├── App.css
│   │   ├── index.js
│   │   └── index.css
│   └── package.json
├── manage.py
├── requirements.txt
├── .gitignore
├── .env.example
└── README.md
```

## 🚀 Установка и запуск

### Шаг 1: Установка Qwen (Ollama)
```bash
# Установите Ollama
curl -fsSL https://ollama.com/install.sh | sh

# Скачайте модель Qwen
ollama pull qwen2.5:7b

# Запустите сервер (оставьте этот терминал открытым)
ollama serve
```

### Шаг 2: Настройка Backend (Django)
```bash
# Клонируйте или создайте папку проекта
cd travel_agency

# Создайте виртуальное окружение
python3 -m venv venv

# Активируйте виртуальное окружение
# Linux/Mac:
source venv/bin/activate
# Windows:
venv\Scripts\activate

# Установите зависимости
pip install -r requirements.txt

# Выполните миграции
python manage.py makemigrations
python manage.py migrate

# Создайте суперпользователя (опционально)
python manage.py createsuperuser

# Заполните БД тестовыми данными
python manage.py populate_tours

# Запустите Django сервер (оставьте этот терминал открытым)
python manage.py runserver
```

Backend будет доступен на `http://localhost:8000`

### Шаг 3: Настройка Frontend (React)

Откройте **новый терминал**:
```bash
# Перейдите в папку frontend
cd travel_agency/frontend

# Установите зависимости
npm install

# Запустите React development сервер
npm start
```

Frontend автоматически откроется на `http://localhost:3000`

## 🎮 Использование

1. Откройте браузер на `http://localhost:3000`
2. Нажмите на кнопку **"🤖 Подобрать тур с AI"** или на плавающую кнопку чата 💬
3. Начните диалог с AI-помощником:
   - "Хочу на пляж"
   - "Покажи экскурсионные туры в Европу"
   - "Бюджет до 100000 рублей"
4. AI подберёт туры и даст рекомендации

## 📡 API Endpoints

### Tours
- `GET /api/tours/` - Получить все туры
- `GET /api/tours/{id}/` - Получить конкретный тур
- `GET /api/tours/?type=beach` - Фильтр по типу тура
- `GET /api/tours/?destination=EU` - Фильтр по направлению
- `GET /api/tours/?min_price=50000&max_price=100000` - Фильтр по цене

### Chat
- `POST /api/chat/` - Отправить сообщение AI
```json
  {
    "message": "Хочу на море",
    "session_id": "optional-session-id"
  }
```
  Ответ:
```json
  {
    "response": "AI ответ",
    "session_id": "session-id",
    "suggested_tours": [...]
  }
```

- `GET /api/chat/history/{session_id}/` - Получить историю чата
- `DELETE /api/chat/clear/{session_id}/` - Очистить историю

## ⚙️ Настройка Qwen

### Для Ollama (рекомендуется)

В `backend/settings.py`:
```python
QWEN_API_URL = 'http://localhost:11434/v1/chat/completions'
QWEN_API_KEY = ''
```

### Для других API (vLLM, llama.cpp и т.д.)

Создайте файл `.env` (скопируйте из `.env.example`):
```bash
QWEN_API_URL=http://your-server:port/v1/chat/completions
QWEN_API_KEY=your-api-key-if-needed
```

## 🗄️ Модели данных

### Tour (Тур)
- `name` - Название тура
- `destination` - Направление (EU, AS, AF, NA, SA, OC)
- `country` - Страна
- `city` - Город
- `tour_type` - Тип (beach, excursion, active, wellness, cruise)
- `duration_days` - Длительность в днях
- `price` - Цена
- `description` - Описание
- `includes` - Что включено
- `rating` - Рейтинг (0-5)
- `available` - Доступен ли тур

### ChatHistory (История чата)
- `session_id` - ID сессии
- `user_message` - Сообщение пользователя
- `ai_response` - Ответ AI
- `created_at` - Время создания

## 🎨 Кастомизация

### Изменение системного промпта AI

Отредактируйте метод `get_system_prompt()` в `tours/ai_service.py`:
```python
def get_system_prompt(self, tours_context):
    return f"""Ваш кастомный промпт здесь..."""
```

### Добавление новых туров

**Через Django Admin:**
1. Перейдите на `http://localhost:8000/admin`
2. Войдите с учетными данными суперпользователя
3. Добавьте новые туры

**Через Django Shell:**
```python
python manage.py shell

from tours.models import Tour

Tour.objects.create(
    name='Название тура',
    destination='EU',
    country='Страна',
    city='Город',
    tour_type='beach',
    duration_days=7,
    price=100000,
    description='Описание',
    includes='Что включено',
    rating=4.5
)
```

### Настройка параметров AI

В `tours/ai_service.py`, метод `chat()`:
```python
payload = {
    "model": "qwen",
    "messages": messages,
    "temperature": 0.7,      # Креативность (0-1)
    "max_tokens": 500,       # Макс. длина ответа
}
```

## 🔧 Troubleshooting

### Проблема: "Connection refused" при обращении к Qwen

**Решение:**
- Убедитесь, что Ollama запущен: `ollama serve`
- Проверьте URL в settings.py
- Убедитесь, что модель скачана: `ollama list`

### Проблема: CORS ошибки

**Решение:**
- Убедитесь, что `django-cors-headers` установлен
- Проверьте `CORS_ALLOWED_ORIGINS` в `settings.py`

### Проблема: Frontend не подключается к Backend

**Решение:**
- Проверьте, что Django запущен на порту 8000
- Проверьте `proxy` в `frontend/package.json`

### Проблема: Туры не загружаются

**Решение:**
```bash
# Выполните миграции
python manage.py migrate

# Заполните БД
python manage.py populate_tours
```

## 📦 Production Deployment

Для production окружения:

1. **Измените настройки Django:**
```python
# settings.py
DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com']
SECRET_KEY = os.getenv('SECRET_KEY')
```

2. **Используйте PostgreSQL вместо SQLite:**
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'travel_db',
        'USER': 'postgres',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

3. **Соберите статику:**
```bash
python manage.py collectstatic
```

4. **Соберите React:**
```bash
cd frontend
npm run build
```

5. **Используйте Gunicorn + Nginx**

## 📝 TODO / Идеи для улучшения

- [ ] Добавить аутентификацию пользователей
- [ ] Реализовать бронирование туров
- [ ] Добавить систему оплаты
- [ ] Улучшить алгоритм подбора туров (векторный поиск)
- [ ] Добавить загрузку изображений туров
- [ ] Реализовать отзывы и рейтинги
- [ ] Добавить мультиязычность
- [ ] Email уведомления
- [ ] Интеграция с картами (Google Maps)

## 📄 Лицензия

MIT License

## 👨‍💻 Автор

Создано с помощью Claude AI

## 🤝 Поддержка

Если возникли вопросы:
1. Проверьте раздел Troubleshooting
2. Убедитесь, что все зависимости установлены
3. Проверьте, что все три сервиса запущены (Ollama, Django, React)
