#!/bin/bash

echo "🚀 Запуск проекта туристической компании..."

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
NC='\033[0m'

# Check if Ollama is running
if ! curl -s http://localhost:11434/api/tags > /dev/null 2>&1; then
    echo -e "${RED}❌ Ollama не запущен!${NC}"
    echo "Запустите Ollama в отдельном терминале:"
    echo "  ollama serve"
    exit 1
fi

# Activate venv and start Django
echo -e "${BLUE}🔧 Запуск Django...${NC}"
source venv/bin/activate
python manage.py runserver &
DJANGO_PID=$!

# Wait for Django to start
sleep 3

# Start React
echo -e "${BLUE}⚛️  Запуск React...${NC}"
cd frontend
npm start &
REACT_PID=$!

echo -e "${GREEN}✅ Проект запущен!${NC}"
echo ""
echo "Django: http://localhost:8000"
echo "React:  http://localhost:3000"
echo ""
echo "Для остановки нажмите Ctrl+C"

# Wait for user interrupt
wait
