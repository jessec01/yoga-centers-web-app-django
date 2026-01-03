# Comandos rápidos — Docker + Django (migraciones y usuario personalizado)

Resumen de comandos útiles para comprobar y reparar migraciones y problemas del modelo de usuario cuando se usa Docker.

Prerequisito: ejecutar desde la raíz del repositorio (/home/jessec/Documentos/yoga-centers-web-app-django).

1) Comprobar presencia de migraciones en el host

```bash
pwd
ls -la userYC/migrations
```

2) Ver qué ve el contenedor

```bash
docker compose exec web pwd
docker compose exec web ls -la /app/userYC/migrations
docker compose exec web python manage.py showmigrations userYC
```

3) Reconstruir imagen (si cambiaste `requirements.txt`)

```bash
docker compose down
docker compose build --no-cache
docker compose up -d
```

4) Crear y aplicar migraciones

```bash
docker compose exec web python manage.py makemigrations userYC
docker compose exec web python manage.py showmigrations userYC
docker compose exec web python manage.py migrate
```

5) Diagnóstico del historial de migraciones

```bash
docker compose exec web python manage.py showmigrations
# Consultar tabla django_migrations en la BD (ajusta variables si son distintas)
docker compose exec db psql -U $POSTGRES_USER -d $POSTGRES_DB -c "select app,name,applied from django_migrations order by applied;"
```

6) Reconciliar migraciones (hacer backup antes)

```bash
# Backup de la BD
docker compose exec db pg_dump -U $POSTGRES_USER $POSTGRES_DB > /tmp/db-backup.sql

# Intentar deshacer admin y aplicar userYC en orden
docker compose exec web python manage.py migrate admin zero
docker compose exec web python manage.py migrate userYC
docker compose exec web python manage.py migrate admin

# Si las tablas ya existen y estás seguro, marcar migración como aplicada (con cuidado)
docker compose exec web python manage.py migrate userYC --fake
```

7) Comprobar `AUTH_USER_MODEL` y configuración

```bash
docker compose exec web python -c "from django.conf import settings; print(settings.AUTH_USER_MODEL)"
# Ver nombre de AppConfig
docker compose exec web python -c "import importlib; m=importlib.import_module('userYC.apps'); print(m.UserycConfig.name)"
```

8) ¿Qué revisar si Django no detecta migraciones?
- Asegúrate que `userYC/migrations/0001_initial.py` exista en el host y en `/app/userYC/migrations` dentro del contenedor.
- Asegúrate que `userYC` está en `INSTALLED_APPS` y `userYC/apps.py` tiene `name='userYC'`.
- Revisa errores de import en `userYC/models.py` (p. ej. dependencias faltantes) — un error de import impide que Django cargue la app y encuentre migraciones.

---
Archivo generado automáticamente. Si quieres lo junto al `README.md` principal o lo incorporo como sección en `README.md`, indícamelo.