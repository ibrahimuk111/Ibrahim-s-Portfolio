# Dockerfile for The Core Memory Bank (PDF Document Q&A)
# Author: Muhammad Ibrahim | ukibrahim111@gmail.com

FROM python:3.11-slim

LABEL maintainer="Muhammad Ibrahim <ukibrahim111@gmail.com>"
LABEL project="The Core Memory Bank (PDF Document Q&A)"

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000 8501

CMD ["python", "app.py"]
