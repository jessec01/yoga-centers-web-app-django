# ErrorModel — Migraciones y modelo de usuario (userYC)

## Resumen ejecutivo

Se produjo un fallo por la ausencia de la librería `phonenumbers` que impedía cargar `phonenumber_field`. Tras añadir la dependencia y reconstruir la imagen apareció una inconsistencia de migraciones: Django indicó que `admin.0001_initial` estaba aplicada antes de su dependencia `userYC.0001_initial`. Además, `showmigrations` devolvía `(no migrations)` para `userYC` porque el contenedor no veía `userYC/migrations/0001_initial.py` debido a un montaje incorrecto del volumen (se ejecutó `docker compose` desde una subcarpeta).

## Causa raíz (ordenada)

1. Falta de dependencia `phonenumbers` en la imagen Docker.
2. Volumen Docker montado desde una subcarpeta (`yogacenterwebapp`) en lugar de la raíz del repo, provocando que el contenedor no vea archivos de migración del host.
3. Migraciones aplicadas en la base de datos en un orden que viola dependencias declaradas por las migraciones.

## Cómo reproducir paso a paso (resumen)

1. Build/Up de Docker desde una carpeta parcial (volumen mal montado).
2. Django arranca y no importa `phonenumbers` → error de import.
3. Se corrige requirements y se rebuild; Django detecta migraciones pendientes pero el contenedor no muestra los archivos de migración (no están en `/app/...`).
4. Al levantar desde la raíz, el archivo `0001_initial.py` aparece y es necesario aplicar la migración; si la tabla `django_migrations` registra migraciones en orden incorrecto aparece `InconsistentMigrationHistory`.

## Solución paso a paso (comandos reproducibles)

A. Reparar dependencias y reconstruir imagen

```bash
# En la raíz del repo
# 1) Añadir a requirements.txt:
#    phonenumbers

docker compose build --no-cache
docker compose up -d
```

B. Comprobar sincronización host ↔ contenedor

```bash
# En el host (desde la raíz del repo)
pwd
ls -la userYC/migrations

# En el contenedor
docker compose exec web pwd
docker compose exec web ls -la /app/userYC/migrations
```

C. Si el contenedor no ve las migraciones: levantar desde la raíz

```bash
docker compose down
# (opcional) docker compose build --no-cache
docker compose up -d
```

D. Crear y aplicar migraciones si falta/si hay que regenerar

```bash
docker compose exec web python manage.py makemigrations userYC
docker compose exec web python manage.py showmigrations userYC
docker compose exec web python manage.py migrate
```

E. Diagnóstico de historial inconsistente (si aparece `InconsistentMigrationHistory`)

```bash
docker compose exec web python manage.py showmigrations
# Ver tabla django_migrations (ajusta credenciales de entorno si fuesen otras)
docker compose exec db psql -U $POSTGRES_USER -d $POSTGRES_DB -c "select app,name,applied from django_migrations order by applied;"
```

F. Reconciliar sin perder datos (hacer backup antes)

```bash
# Backup
docker compose exec db pg_dump -U $POSTGRES_USER $POSTGRES_DB > /tmp/db-backup.sql

# Intentar deshacer admin y aplicar en orden
docker compose exec web python manage.py migrate admin zero
docker compose exec web python manage.py migrate userYC
docker compose exec web python manage.py migrate admin

# Si no es posible, usar --fake con extremo cuidado
# (solo si sabes que las tablas existen y coinciden con las migraciones)
docker compose exec web python manage.py migrate userYC --fake
```

## Comprobaciones que siempre realizar antes de cambiar historia de migraciones

- Hacer dump/backup de la BD.
- Revisar `INSTALLED_APPS` y `userYC/apps.py` (`name='userYC'`).
- Ver que `userYC/migrations/__init__.py` existe y que `0001_initial.py` está presente y correcto.
- Ejecutar `showmigrations` y revisar `django_migrations` en la BD.

## Puntos concretos de código a revisar

- `yogacenterwebapp/settings.py`: `INSTALLED_APPS` y `AUTH_USER_MODEL = 'userYC.UserYogaCenter'`.
- `userYC/models.py`: `class UserYogaCenter(AbstractUser)` y `phone = PhoneNumberField(...)`.
- `userYC/apps.py`: `name = 'userYC'`.
- `requirements.txt`: incluir `django-phonenumber-field` y `phonenumbers`.

## Referencias para estudiar (autonomía)

- Django Migrations: https://docs.djangoproject.com/en/stable/topics/migrations/
- `migrate` options (`--fake`, `zero`): https://docs.djangoproject.com/en/stable/ref/django-admin/#migrate
- Custom user model: https://docs.djangoproject.com/en/stable/topics/auth/customizing/#substituting-a-custom-user-model
- django-phonenumber-field: https://github.com/stefanfoulis/django-phonenumber-field
- phonenumbers (PyPI): https://pypi.org/project/phonenumbers/
- Docker Volumes: https://docs.docker.com/storage/volumes/
- PostgreSQL backup: https://www.postgresql.org/docs/current/backup-dump.html

## Conclusión (resumen breve)

El fallo fue una conjunción de dependencias faltantes y un montaje erróneo del volumen Docker que provocó que el contenedor no viera archivos de migración del host. La solución consistió en:

- Añadir `phonenumbers` a `requirements.txt` y reconstruir la imagen.
- Asegurarse de ejecutar `docker compose` desde la raíz del repositorio (o corregir la ruta del volumen) para que `/app` contenga todos los archivos.
- Aplicar las migraciones en el orden correcto; si la historia está inconsistente, hacer backup y reconciliar con `migrate ... zero` y/o `--fake` según el caso.

Si quieres, guardo este documento como `errormodel.md` en la raíz del repositorio y puedo además crear un `README` pequeño con los comandos rápidos. ¿Lo guardo ahora?