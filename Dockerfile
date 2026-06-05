FROM python:3.14-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY pyproject.toml ./
COPY creds.py ./
COPY practice/ ./practice/
COPY tests/ ./tests/

CMD ["pytest", "-v"]
