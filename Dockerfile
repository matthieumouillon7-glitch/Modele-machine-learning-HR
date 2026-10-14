FROM python:3.12-slim

WORKDIR /app

COPY .streamlit/api/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY .streamlit/api/ ./.streamlit/api/
COPY streamlit/Modèle/weather_artifacts.joblib ./streamlit/Modèle/weather_artifacts.joblib

EXPOSE 8080

CMD ["sh", "-c", "uvicorn main:app --app-dir /app/.streamlit/api --host 0.0.0.0 --port ${PORT:-8080}"]
