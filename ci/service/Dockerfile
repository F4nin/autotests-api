FROM python:3.11-slim

WORKDIR /app

# Установка git и curl
RUN apt-get update && \
    apt-get install -y git curl && \
    rm -rf /var/lib/apt/lists/*

# Клонируем сервис
RUN git clone https://github.com/F4nin/qa-automation-engineer-api-course.git .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Создаем .env файл и добавляем в него переменные
RUN echo 'APP_HOST="http://api-service:8000"' >> .env && \
    echo 'DATABASE_URL="sqlite+aiosqlite:///./local.db"' >> .env && \
    echo 'JWT_ALGORITHM="HS256"' >> .env && \
    echo 'JWT_SECRET_KEY="qa-automation-engineer-api-course-secret-key"' >> .env && \
    echo 'JWT_ACCESS_TOKEN_EXPIRE=1800' >> .env && \
    echo 'JWT_REFRESH_TOKEN_EXPIRE=5184000' >> .env

# Открываем порт (FastAPI по умолчанию 8000)
EXPOSE 8000

# Запускаем сервер с uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]