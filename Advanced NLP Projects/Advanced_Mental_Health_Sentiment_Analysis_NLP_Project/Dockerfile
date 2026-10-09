# Dockerfile for Advanced_Mental_Health_Sentiment_Analysis_NLP_Project
# Author: Muhammad Ibrahim | ukibrahim111@gmail.com

FROM python:3.11-slim

LABEL maintainer="Muhammad Ibrahim <ukibrahim111@gmail.com>"
LABEL project="Advanced_Mental_Health_Sentiment_Analysis_NLP_Project"

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000 8501

CMD ["python", "app.py"]
