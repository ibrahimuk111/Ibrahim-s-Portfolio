# Dockerfile for Advanced_Human_vs_AI_Text_Classifier_using_NLP_and_BERT
# Author: Muhammad Ibrahim | ukibrahim111@gmail.com

FROM python:3.11-slim

LABEL maintainer="Muhammad Ibrahim <ukibrahim111@gmail.com>"
LABEL project="Advanced_Human_vs_AI_Text_Classifier_using_NLP_and_BERT"

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000 8501

CMD ["python", "app.py"]
