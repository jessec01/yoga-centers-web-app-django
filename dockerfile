# 1. Imagen base
FROM python:3.11-slim-bookworm
# 2. Metadatos
#se corregira el formato de los labels
LABEL version="1.0"
LABEL description="Dockerfile for a secure and efficient Django application deployment."
LABEL maintenance="Jessec Zuleta, Daniel N"
# 3. Directorio de trabajo
#se incluira los PYTHONDONTWRITEBYTECODE y PYTHONUNBUFFERED
#despues de testear la aplicacion
WORKDIR /app
#4 copiamos el archivo de requerimientos
COPY requirements.txt .
#5 instalar dependencias del sistema (¡como root!)
RUN pip install --no-cache-dir -r requirements.txt
#6 instalo  curl 
#¡como root!
#actualizo la lista de paquetes e instalo curl
#luego limpio la cache de apt para reducir el tamaño de la imagen
#especifico la version de curl para mayor seguridad
#limpio los archivos temporales de apt
RUN  apt-get update && apt-get install -y  --no-install-recommends curl  \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*
# 8. Copiar el resto de tu código (como root)
COPY . .
# 6. Crear el usuario no-root (como root)
RUN groupadd -r django_group \ 
&& useradd -r -g django_group django_user \ 
&& chown -R django_user:django_group /app
USER django_user
EXPOSE 8000
#Defino mi healteach
HEALTHCHECK --interval=30s --timeout=3s --retries=3 \ 
CMD curl -f http://localhost:8000/health 
# 11. Definir el punto de entrada
#en produccion se recomienda usar gunicorn o daphne
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]