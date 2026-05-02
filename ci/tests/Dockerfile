FROM python:3.13-slim

WORKDIR /tests

# Установка git
RUN apt-get update && \
    apt-get install -y git && \
    rm -rf /var/lib/apt/lists/*

ARG REPO_URL=https://github.com/F4nin/autotests-api.git
ARG BRANCH=main

# Клонируем проект
RUN git clone -b $BRANCH $REPO_URL .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Создаем .env файл и добавляем в него переменные
RUN echo "BASE_URL=http://api-service:8000" > .env && \
    echo "API_URL=http://api-service:8000" >> .env && \
    echo "APP_HOST=http://api-service:8000" >> .env && \
    echo "TEST_DATA.IMAGE_PNG_FILE=./testdata/files/image.png" >> .env && \
    echo "HTTP_CLIENT.URL=http://api-service:8000" >> .env && \
    echo "HTTP_CLIENT.TIMEOUT=100" >> .env

# Создаём папку для Allure
RUN mkdir -p allure-results

CMD ["sh", "-c", "pytest -m \"${PYTEST_MARKERS:-regression}\" -v --alluredir=/app/allure-results"]