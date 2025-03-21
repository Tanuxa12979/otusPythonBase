FROM python:3.12-bookworm

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /var/app

ENV PIP_NO_VIRTUALENV=1

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY  . .

EXPOSE 8000

#CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

CMD ["gunicorn", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "homework_04.main:app", "-b", "0.0.0.0:8000"]

