#!/bin/sh



# -------------------
# Esperar a que PostgreSQL esté listo
echo "Waiting for a PostgreSQL..."
while ! nc -z db 5432; do
  sleep 0.1
done
echo "PostgreSQL is ready"

# Ejecutar migraciones
echo "Executing migrations..."
python manage.py migrate

# Ejecutar comando principal
exec "$@"