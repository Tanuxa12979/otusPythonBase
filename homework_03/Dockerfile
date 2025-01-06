#docker build -t homework_05_docker -f homework_03/Dockerfile . - создание контейнера
#docker run -d -p 8000:8000 homework_05_docker - запуск контейнера

FROM python:3.9-buster

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "homework_03.app:app", "--host", "0.0.0.0", "--port", "8000"]