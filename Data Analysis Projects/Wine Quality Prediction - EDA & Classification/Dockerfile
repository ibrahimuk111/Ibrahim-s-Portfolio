# Dockerfile for Wine Quality Prediction - EDA & Classification
# Author: Muhammad Ibrahim | ukibrahim111@gmail.com

FROM python:3.11-slim

LABEL maintainer="Muhammad Ibrahim <ukibrahim111@gmail.com>"
LABEL project="Wine Quality Prediction - EDA & Classification"

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000 8501

CMD ["python", "app.py"]
