FROM python:3.14-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app/main.py .

CMD ["uvicorn", "app.main:app"]