# TEST UNITARIO YOGUI

## Resumen

Este archivo documenta la ejecución del test unitario para la app `yogui`. El contenido principal lo redactarás tú; aquí se incluye un resumen automático de la falla y secciones para completar.
## casos de prueba
abrir:
 ``` python manage.py shell ```
primero importar las librería

 ``` from tu_app.models import 
#se debe importar los modelos del usuario, yogui e instructor
from django.db import IntegrityError
#esta para validacion ``` 


prueba número 1
 ```
# Definimos el usuario en una variable 'u'
u = YogaCenterUser.objects.create_user(
    username="prueba_manual",
    password="123",
    email="test@yoga.com",
    first_name="Juan",
    phone="+584121234567"
)

# Validamos que se creó:
print(u.id)
# Debería salir un número (ej: 1)

print(u.phone)
# Debería salir: +584121234567 ```

prueba número 2

 ```
# Creamos el Yogi vinculándolo a la variable 'u' que creamos arriba
y = Yogi.objects.create(
    user=u, 
    urlprofile="foto_yogi.jpg"
)

# Validamos que existe:
print(y.id)

print(y.user.first_name)
# Debería responder: "Juan" ```



# Validamos:
print(i.rating)
# Debería salir: 4.5 ```

prueba número 4 
 ```
# Intentamos asignar el rol al usuario ID 9999 (que no existe)
try:
    Yogi.objects.create(user_id=9999, urlprofile="fantasma.jpg")
except IntegrityError:
    print("¡PRUEBA EXITOSA! La base de datos impidió crear un rol huérfano.")
except Exception as e:
    print(f"Ocurrió otro error: {e}") ```
## Consideraciones 

Se desarrollo directamente un test unitario para validar el comportamiento del modelo yogui.

## Salida de la prueba (resumen automático)

```
Found 2 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
..E
======================================================================
ERROR: test_validation_integration (yogui.tests.YoguiProfileModelTest.test_validation_integration)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/site-packages/django/db/backends/utils.py", line 103, in _execute
    return self.cursor.execute(sql)
           ^^^^^^^^^^^^^^^^^^^^^^^^
psycopg2.errors.ForeignKeyViolation: insert or update on table "yogui_profile" violates foreign key constraint "yogui_yoguiprofile_user_id_82b72fa3_fk_user_yoga_center_id"
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
django.db.utils.IntegrityError: insert or update on table "yogui_profile" violates foreign key constraint "yogui_yoguiprofile_user_id_82b72fa3_fk_user_yoga_center_id"
DETAIL:  Key (user_id)=(9999) is not present in table "user_yoga_center".


----------------------------------------------------------------------
Ran 2 tests in 0.006s

FAILED (errors=1)
```

## Instrucciones para reproducir

- Desde Docker (recomendado):

```
docker compose exec web python3 manage.py test
```

- Desde entorno virtual local:

```
source venv/bin/activate
python3 manage.py test
```

## Posibles causas (marcador)

- Datos de prueba mal preparados: la prueba intenta guardar una `YoguiProfile` referenciando un `user_id` que no existe en la tabla `user_yoga_center`.
- Fixtures o factories que no crean la entidad referenciada.

## Secciones que debes redactar

- **Objetivo del test:** (tu texto)
- **Pasos detallados para reproducir:** (tu texto)
- **Causa raíz identificada:** (tu texto)
- **Solución propuesta / cambios sugeridos en el código o tests:** (tu texto)
- **Notas adicionales / referencias:** (tu texto)

---

Si quieres, puedo proponerte un borrador para cualquiera de las secciones anteriores o intentar arreglar la prueba y volver a ejecutar los tests.
