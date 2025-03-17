FROM python:3.9-slim-bookworm

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /var/app

ENV PIP_NO_VIRTUALENV=1

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY  . .

EXPOSE 8000

CMD ["uvicorn", "homework_04\main:app", "--host", "0.0.0.0", "--port", "8000"]

