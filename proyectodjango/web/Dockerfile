# Usamos una imagen de Python 3
FROM python:3.8

# Establecemos un directorio de trabajo
WORKDIR /code

# Copiamos requirements.txt al contenedor
COPY requirements.txt .

# Instalamos las dependencias de Python
RUN pip install -r requirements.txt

# Copiamos el resto del código al contenedor
COPY . .

# Exponemos el puerto donde correrá Gunicorn
EXPOSE 8000

# Comando para iniciar Gunicorn
CMD ["gunicorn", "myproject.wsgi:application", "--bind", "0.0.0.0:8000"]
