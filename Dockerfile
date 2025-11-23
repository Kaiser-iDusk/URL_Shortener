FROM python:3.12-slim

WORKDIR /url_shortener

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
EXPOSE 5000

CMD ["flask", "--app", "main", "run", "--host=0.0.0.0", "--port=5000"]