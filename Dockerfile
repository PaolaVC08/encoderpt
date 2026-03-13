FROM python:3.10-slim 

# Usamos -slim para que la imagen pese menos (Torch es pesado)
WORKDIR /app

COPY requirements.txt .
# Instalamos la versión de CPU de torch para que no pese GBs innecesarios en Render
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Render ignorará EXPOSE, pero es buena práctica
EXPOSE 10000

# Usamos Gunicorn para producción y bindeamos al puerto que nos dé Render
CMD ["sh", "-c", "gunicorn --bind 0.0.0.0:$PORT app:app"]
