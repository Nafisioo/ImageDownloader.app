FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install PostgreSQL client libraries
RUN apt-get update && apt-get install -y postgresql-client libpq-dev

COPY . .

ENV DB_HOST=myhost
ENV DB_PORT=5432
ENV DB_USER=postgres
ENV DB_PASS=13840131
ENV DB_NAME=myimg.db

EXPOSE 5000

CMD ["python", "app.py"]