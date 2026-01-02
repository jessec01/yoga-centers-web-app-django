# TEST UNITARIO CENTER_ADMINISTRATOR

## Resumen

Este documento recoge la ejecución del test unitario para la app `center_administrator`. Incluye la salida del test proporcionada, diagnóstico inicial, pasos sugeridos y secciones para que completes el análisis.

## Salida de la prueba (output proporcionado)

```
Found 2 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
..E
======================================================================
ERROR: test_validation_integration (center_administrator.tests.CenterAdministratorProfileModelTest.test_validation_integration)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/site-packages/django/db/backends/utils.py", line 103, in _execute
    return self.cursor.execute(sql)
           ^^^^^^^^^^^^^^^^^^^^^^^^
psycopg2.errors.ForeignKeyViolation: insert or update on table "center_administrator" violates foreign key constraint "center_administrator_user_id_48bff6d8_fk_userYC_us"
DETAIL:  Key (user_id)=(9999) is not present in table "user_yoga_center".

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/usr/local/lib/python3.11/site-packages/django/db/backends/postgresql/base.py", line 482, in check_constraints
    cursor.execute("SET CONSTRAINTS ALL IMMEDIATE")
```

## Instrucciones para reproducir

- Desde Docker (recomendado):

```
docker compose exec web python3 manage.py test center_administrator
```

- Desde entorno virtual local:

```
source venv/bin/activate
python3 manage.py test center_administrator
```

## Diagnóstico inicial / Posibles causas

- Datos de prueba mal preparados: la prueba intenta crear o actualizar una entidad `center_administrator` referenciando un `user_id` (9999) que no existe en la tabla `user_yoga_center`.
- Fixtures o factories que no crean la entidad `UserYogaCenter` necesaria.
- Valores hardcodeados en el test que asumen ID existentes en la BD de pruebas.
- Migraciones/desincronización: la estructura de tablas puede no coincidir con lo esperado por el test.

