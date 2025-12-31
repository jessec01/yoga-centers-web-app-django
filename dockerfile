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
#convierte  las variables de entorno para python
#en configuraciones optimas para aplicaciones web
#rpython no escribira archivos .pyc
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
#definir las variables de entorno para el usuario no root
ARG UID=1000
ARG GID=1000
# 6. Crear el usuario no-root (como root)
RUN groupadd -g $GID django_group  && \
 useradd -l -u $UID -g django_group django_user 
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
#buena practica definir la version de los paquetes
#en esta caso se usa la version 7.88.1-10+deb12u14 de curl es la ultima version estable
#Se soluciono problemas de seguridad relacionados con versiones antiguas de curl
#Problema corrigido con la versiones no especifica para la 
#para la version de python:3.11-slim-bookworm
RUN  apt-get update && apt-get install -y  --no-install-recommends curl=7.88.1-10+deb12u14  \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*
# 8. Copiar el resto de tu código (como root)
COPY . .

# Define los permiso la sincronizacion de archivos del contenedor al host
RUN chown -R django_user:django_group /app
USER django_user
EXPOSE 8000
#Defino mi healteach
#al definir una ruta de healthcheck en mi aplicacion
#me aseguro que el contenedor este funcionando correctamente
#y pueda responder a las solicitudes
#se debe asegurar que la ruta /health este implementada en la aplicacion django
HEALTHCHECK --interval=30s --timeout=3s --retries=3 \ 
CMD curl -f http://localhost:8000/health/ 

# 11. Definir el punto de entrada
#en produccion se recomienda usar gunicorn o daphne
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]