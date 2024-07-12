FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install PostgreSQL client libraries
RUN apt-get update && apt-get install -y libpq-dev

COPY . .

CMD ["python", "app.py"]