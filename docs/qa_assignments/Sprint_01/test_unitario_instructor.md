# TEST UNITARIO INSTRUCTOR

## Resumen

Este documento recoge la ejecución del test unitario para la app `instructor`. Incluye la salida del test, posibles causas y secciones para que completes el análisis.

## Salida de la prueba (output proporcionado)

```
Found 1 test(s).
System check identified no issues (0 silenced).
E
======================================================================
ERROR: instructor.tests (unittest.loader._FailedTest.instructor.tests)
----------------------------------------------------------------------
ImportError: Failed to import test module: instructor.tests
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/unittest/loader.py", line 419, in _find_test_path
    module = self._get_module_from_name(name)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/unittest/loader.py", line 362, in _get_module_from_name
    __import__(name)
  File "/app/instructor/tests.py", line 4, in <module>
    from .models import YoguiProfile
ImportError: cannot import name 'YoguiProfile' from 'instructor.models' (/app/instructor/models.py)


----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (errors=1)
```

## Instrucciones para reproducir

- Desde Docker (recomendado):

```
docker compose exec web python3 manage.py test instructor
```

- Desde entorno virtual local:

```
source venv/bin/activate
python3 manage.py test instructor
```

## Diagnóstico inicial / Posibles causas

- ImportIncorrecto: `tests.py` intenta importar `YoguiProfile` desde `instructor.models`, pero ese símbolo no existe en el archivo `instructor/models.py`.
- Renombrado de modelo: el modelo pudo haber sido renombrado (ej. `YoguProfile`, `InstructorProfile`) sin actualizar los imports.
- Modelo definido en otra app: el modelo realmente pertenece a otra app (ej. `yogui.models`) y el import es incorrecto.
- Error de refactor o eliminación: el modelo fue eliminado o movido y quedan imports huérfanos.
- Circular import: importaciones entre módulos que provocan fallo al importar en tiempo de carga.

## Pasos sugeridos para investigar

1. Abrir `instructor/tests.py` y revisar la línea de import donde aparece `YoguiProfile`.
2. Abrir `instructor/models.py` y comprobar si `YoguiProfile` está definido y correctamente nombrado.
3. Buscar en el repo la definición del modelo para confirmar su app y nombre:

```
grep -R "class .*YoguiProfile" -n || grep -R "class .*Yogi" -n
```

4. Si el modelo pertenece a otra app, corregir el import en `tests.py` (ej. `from yogui.models import YoguiProfile`).
5. Ejecutar nuevamente el test tras corregir el import.

## Secciones que debes redactar

- **Objetivo del test:** (tu texto)
- **Pasos detallados para reproducir:** (tu texto)
- **Salida real completa del test:** (ya incluida arriba)
- **Causa raíz identificada:** (tu texto tras investigar)
- **Solución propuesta / cambios sugeridos en el código o tests:** (tu texto)
- **Notas adicionales / referencias:** (tu texto)

---

¿Quieres que:

- redacte un borrador para la sección "Solución propuesta" con un parche para `instructor/tests.py` si confirmas el nombre correcto del modelo? o
- yo busque en el repositorio el modelo y proponga la corrección del import y aplique el cambio directamente?
