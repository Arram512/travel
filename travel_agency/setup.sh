#!/bin/bash

echo "🚀 Настройка проекта туристической компании..."

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check if Ollama is installed
if ! command -v ollama &> /dev/null
then
    echo -e "${YELLOW}⚠️  Ollama не найден. Установите его:${NC}"
    echo "curl -fsSL https://ollama.com/install.sh | sh"
    exit 1
fi

# Backend setup
echo -e "${BLUE}📦 Настройка Django backend...${NC}"
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

echo -e "${BLUE}🗄️  Создание базы данных...${NC}"
python manage.py makemigrations
python manage.py migrate

echo -e "${BLUE}📝 Заполнение тестовыми данными...${NC}"
python manage.py populate_tours

echo -e "${GREEN}✅ Backend готов!${NC}"
echo ""

# Frontend setup
echo -e "${BLUE}⚛️  Настройка React frontend...${NC}"
cd frontend
npm install

echo -e "${GREEN}✅ Frontend готов!${NC}"
echo ""

echo -e "${GREEN}🎉 Установка завершена!${NC}"
echo ""
echo -e "${YELLOW}Для запуска проекта выполните следующие команды:${NC}"
echo ""
echo "1️⃣  Запустите Ollama с Qwen (в отдельном терминале):"
echo "   ollama pull qwen2.5:7b"
echo "   ollama serve"
echo ""
echo "2️⃣  Запустите Django (в отдельном терминале):"
echo "   source venv/bin/activate"
echo "   python manage.py runserver"
echo ""
echo "3️⃣  Запустите React (в отдельном терминале):"
echo "   cd frontend"
echo "   npm start"
echo ""
echo -e "${GREEN}Сайт будет доступен на http://localhost:3000${NC}"
