# 1. Imagen base
FROM python:3.11-slim-bookworm

# 2. Variables de entorno
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 3. Directorio de trabajo
WORKDIR /app

# 4. Instalar dependencias del sistema (como root)
RUN apt-get update \
    && apt-get install -y netcat-traditional \
    && rm -rf /var/lib/apt/lists/*

# 5. Instalar dependencias de Python (como root)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 6. Crear el usuario no-root (como root)
#    -r = usuario de sistema, -m = crear su home, -s /bin/bash = shell
RUN useradd -r -m -s /bin/bash django

# 7. Copiar el entrypoint y darle permisos (¡como root!)
#    (El error estaba en esta parte)
COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

# 8. Copiar el resto de tu código (como root)
COPY . .

# 9. Darle al usuario 'django' la propiedad de TODO (¡como root!)
RUN chown -R django:django /app

# 10. Cambiar al usuario no-root
#     A partir de aquí, todo se ejecuta como 'django'
USER django

# 11. Definir el punto de entrada
ENTRYPOINT ["sh","/app/entrypoint.sh"]