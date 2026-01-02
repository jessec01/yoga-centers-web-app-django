# TEST UNITARIO SUPER_ADMIN

## Resumen

Este documento recoge la ejecución del test unitario para la app `super_admin`. Incluye la salida del test proporcionada, diagnóstico inicial, pasos sugeridos y secciones para que completes el análisis.

## Salida de la prueba (output proporcionado)

```
Found 2 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
..E
======================================================================
ERROR: test_validation_integration (super_admin.tests.SuperAdminProfileModelTest.test_validation_integration)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/site-packages/django/db/backends/utils.py", line 103, in _execute
    return self.cursor.execute(sql)
           ^^^^^^^^^^^^^^^^^^^^^^^^
psycopg2.errors.ForeignKeyViolation: insert or update on table "super_admin" violates foreign key constraint "super_admin_user_id_4ec2bbd6_fk_userYC_useryogacenter_id"
DETAIL:  Key (user_id)=(9999) is not present in table "user_yoga_center".

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/usr/local/lib/python3.11/site-packages/django/db/backends/postgresql/base.py", line 482, in check_constraints
    cursor.execute("SET CONSTRAINTS ALL IMMEDIATE")
  File "/usr/local/lib/python3.11/site-packages/django/db/backends/utils.py", line 79, in execute
    return self._execute_with_wrappers(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/django/db/backends/utils.py", line 92, in _execute_with_wrappers
    return executor(sql, params, many, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/django/db/backends/utils.py", line 100, in _execute
    with self.db.wrap_database_errors:
  File "/usr/local/lib/python3.11/site-packages/django/db/utils.py", line 91, in __exit__
    raise dj_exc_value.with_traceback(traceback) from exc_value
  File "/usr/local/lib/python3.11/site-packages/django/db/backends/utils.py", line 103, in _execute
    return self.cursor.execute(sql)
           ^^^^^^^^^^^^^^^^^^^^^^^^
django.db.utils.IntegrityError: insert or update on table "super_admin" violates foreign key constraint "super_admin_user_id_4ec2bbd6_fk_userYC_useryogacenter_id"
DETAIL:  Key (user_id)=(9999) is not present in table "user_yoga_center".


----------------------------------------------------------------------
Ran 2 tests in 0.007s

FAILED (errors=1)
Destroying test database for alias 'default'...
```

## Instrucciones para reproducir

- Desde Docker (recomendado):

```
docker compose exec web python3 manage.py test super_admin
```

- Desde entorno virtual local:

```
source venv/bin/activate
python3 manage.py test super_admin
```

## Diagnóstico inicial / Posibles causas

- Datos de prueba mal preparados: el test intenta crear o actualizar una fila en `super_admin` referenciando `user_id=9999` que no existe en `user_yoga_center`.
- Fixtures o factories incompletas que no crean la entidad `UserYogaCenter` necesaria.
- Referencias a IDs hardcodeadas en los tests en lugar de crear objetos y usar sus IDs.
- Cambio o refactor en modelos o migraciones que dejó tests desactualizados.

## Pasos sugeridos para investigar y corregir

1. Abrir `super_admin.tests` y localizar dónde se crea la instancia que usa `user_id=9999`.
2. Verificar si el test usa fixtures, factories o crea el usuario manualmente; en caso de usar ID hardcodeado, reemplazar por creación explícita:

```py
user = UserYogaCenter.objects.create(...)
SuperAdmin.objects.create(user=user, ...)
```

3. Ejecutar sólo el test afectado para iterar rápido:

```
docker compose exec web python3 manage.py test super_admin.tests.SuperAdminProfileModelTest.test_validation_integration
```

4. Asegurar que las migraciones están aplicadas en el contenedor de pruebas si es necesario:

```
docker compose exec web python3 manage.py makemigrations
docker compose exec web python3 manage.py migrate --noinput
```

5. Si usas factories (Factory Boy), verificar que la factory de `UserYogaCenter` esté siendo llamada desde la factory del `SuperAdmin`.

## Secciones que debes redactar

- **Objetivo del test:** (tu texto)
- **Pasos detallados para reproducir:** (tu texto)
- **Salida real completa del test:** (ya incluida arriba)
- **Causa raíz identificada:** (tu texto tras investigar)
- **Solución propuesta / cambios sugeridos en el código o tests:** (tu texto)
- **Notas adicionales / referencias:** (tu texto)

---

¿Quieres que busque en el repositorio el test y las factories/fixtures relacionados y proponga un parche para corregir la preparación de datos? Puedo aplicarlo y volver a ejecutar el test si me das permiso.
