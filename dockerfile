# Используйте официальный образ Python в качестве базового
FROM python:3.11-slim

# Установите рабочий каталог в контейнере
WORKDIR /app

# Скопируйте текущий каталог содержимого в контейнер по пути /app
COPY . /app

# Установите зависимости из requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Определите переменные окружения
ENV PYTHONUNBUFFERED=1

# Определите команду, которая будет выполняться при запуске контейнера
CMD ["python", "bot.py"]
