# Documento de Caso de Uso Y2: Registro

## Introducción

El presente documento tiene como objetivo documentar el caso de uso Y2 correspondiente al registro de usuarios en el sistema YogaCenter. Este documento sigue los estándares establecidos para el proyecto, incluyendo el uso de PEP 8, documentación de Django y Conventional Commits. A continuación, se presenta la conversión del caso de uso en requisitos técnicos específicos que guiarán la implementación del módulo de registro.

El caso de uso de registro es fundamental para el funcionamiento del sistema, ya que representa el primer punto de contacto entre el usuario (Yogui) y la plataforma. Una implementación correcta de este módulo garantiza la seguridad, integridad y usabilidad del sistema completo. Por esta razón, se han establecido estándares estrictos y consideraciones técnicas específicas que deben seguirse durante el desarrollo.

---

## 1. Estándares Aplicables

### 1.1 Estándares de Código

Se exige el uso de todos los estándares para una claridad y un único estilo al código, incluyendo el uso del inglés en todo el apartado de código. Estos estándares son obligatorios para garantizar la mantenibilidad, legibilidad y colaboración efectiva entre desarrolladores.

**Estándares obligatorios:**

- **PEP 8**: Guía de estilo para código Python. Todos los nombres de variables, funciones y clases deben seguir las convenciones establecidas en esta guía. El sangrado debe ser de cuatro espacios por nivel, las líneas no deben superar los 79 caracteres, y las importaciones deben organizarse en grupos lógicos.

- **Documentación de Django**: Toda la documentación del proyecto debe seguir las convenciones oficiales de Django. Esto incluye la estructura de aplicaciones, naming de modelos, vistas y URLs. La documentación inline debe usar el formato docstring de Django.

- **Conventional Commits**: Los mensajes de commit deben seguir el formato conventionalcommits.org. Cada commit debe comenzar con un tipo (feat, fix, docs, style, refactor, test, chore) seguido de una descripción concisa del cambio realizado.

### 1.2 Estándares de Base de Datos

La integridad de los datos es crítica para el módulo de registro. Se deben aplicar las siguientes consideraciones de base de datos para garantizar la consistencia y atomicidad de las operaciones.

- **Transacciones**: Todas las operaciones de registro deben ejecutarse dentro de una transacción de base de datos. Esto evita problemas de atomicidad y race conditions que podrían resultar en datos inconsistentes o usuarios duplicados.

- **Claves foráneas**: Todos los registros de usuario deben estar asociados correctamente con entidades relacionadas (centro, rol). No se debe permitir la creación de usuarios huérfanos ni registros sin las referencias adecuadas.

---

## 2. Especificación del Caso de Uso Y2

### 2.1 Metadatos del Caso de Uso

| Elemento | Descripción |
|----------|-------------|
| **Nombre del Caso de uso** | Registro |
| **Identificador (ID)** | Y2 |
| **Actor principal** | Yogui |
| **Actores secundarios** | Sistema, Centro de Yoga |
| **Descripción** | El Yogui se registra en el sistema proporcionando sus datos personales y credenciales de acceso. |
| **Precondiciones** | El Yogui debe haber ubicado el centro de yoga mediante el caso de uso Y1 (Ubicar centro). |
| **Post condiciones** | El Yogui crea un usuario satisfactoriamente en el sistema con un rol asignado. |

### 2.2 Flujo de Eventos

#### 2.2.1 Flujo Principal

El flujo principal describe la secuencia normal de eventos cuando el registro se realiza correctamente sin errores ni excepciones. Este flujo representa el escenario ideal que debe implementarse y probarse exhaustivamente.

1. El Yogui recibe la información del centro de yoga (obtenida mediante Y1).
2. El sistema muestra el formulario de registro con los campos requeridos.
3. El Yogui ingresa sus datos personales: nombre, apellido, correo electrónico, contraseña y datos adicionales requeridos.
4. El sistema valida que el correo electrónico no exista previamente en la base de datos.
5. El sistema valida que el Yogui cumple con los requisitos del centro (edad mínima, documentación, etc.).
6. El Yogui confirma su registro.
7. El sistema crea el usuario dentro de una transacción atómica.
8. El sistema asigna el rol correspondiente al usuario.
9. El sistema redirige al Yogui a la página de inicio de sesión (Y3).
10. El registro se completa exitosamente.

#### 2.2.2 Flujo Alterno

El flujo alterno describe las situaciones excepcionales que pueden ocurrir durante el proceso de registro. El sistema debe manejar cada una de estas situaciones de manera apropiada, proporcionando mensajes de error claros y orientando al usuario hacia la resolución del problema.

1. El Yogui no cumple con los requisitos del centro para registrarse.
   - **Edad insuficiente**: El sistema muestra un mensaje indicando que no cumple con la edad mínima requerida.
   - **Sin correo electrónico válido**: El sistema valida el formato del correo y rechaza direcciones inválidas.
   - **Documentación incompleta**: El sistema indica qué documentos adicionales son requeridos.
2. El correo electrónico ya está registrado en el sistema.
   - El sistema muestra un mensaje indicando que el correo ya existe.
   - El sistema ofrece la opción de recuperar la contraseña.
3. Error de conexión durante el registro.
   - El sistema revierte la transacción y muestra un mensaje de error.
   - El usuario puede intentar nuevamente sin duplicación de datos.

---

## 3. Requisitos Técnicos de Implementación

### 3.1 Requisitos Funcionales

Los requisitos funcionales definen las capacidades específicas que el módulo de registro debe proporcionar. Cada requisito está vinculado a una o más funcionalidades del caso de uso y debe ser implementado de acuerdo con los estándares establecidos.

| ID Requisito | Descripción | Prioridad | Caso de Uso Relacionado |
|--------------|-------------|-----------|-------------------------|
| RF-Y2-001 | El sistema debe permitir el registro de nuevos usuarios con correo electrónico único | Alta | Y2 |
| RF-Y2-002 | El sistema debe validar el formato del correo electrónico antes de registrar | Alta | Y2 |
| RF-Y2-003 | El sistema debe verificar que el correo electrónico no exista previamente en la base de datos | Alta | Y2 |
| RF-Y2-004 | El sistema debe implementar validación de edad mínima según requisitos del centro | Media | Y2 |
| RF-Y2-005 | El sistema debe crear el usuario dentro de una transacción atómica | Alta | Y2 |
| RF-Y2-006 | El sistema debe asignar el rol correspondiente al usuario automáticamente | Alta | Y2 |
| RF-Y2-007 | El sistema debe mostrar mensajes de error claros en caso de fallos | Media | Y2 |
| RF-Y2-008 | El sistema debe permitir la navegación al caso de uso Y1 desde el formulario de registro | Baja | Y2, Y1 |
| RF-Y2-009 | El sistema debe redirigir al usuario al caso de uso Y3 después de un registro exitoso | Alta | Y2, Y3 |

### 3.2 Requisitos No Funcionales

Los requisitos no funcionales definen las características de calidad que el módulo de registro debe cumplir. Estos requisitos son críticos para garantizar una experiencia de usuario satisfactoria y la seguridad del sistema.

| ID Requisito | Descripción | Métrica |
|--------------|-------------|---------|
| RNF-Y2-001 | El tiempo de respuesta del formulario de registro no debe exceder 2 segundos | < 2 segundos |
| RNF-Y2-002 | La contraseña debe almacenarse de forma encriptada utilizando algoritmos seguros | bcrypt/argon2 |
| RNF-Y2-003 | El sistema debe manejar concurrentemente múltiples registros simultáneos | 100+ registros/minuto |
| RNF-Y2-004 | Los datos sensibles deben transmitirse únicamente a través de HTTPS | TLS 1.3 |
| RNF-Y2-005 | El sistema debe proporcionar retroalimentación visual durante el proceso de registro | < 500ms |

---

## 4. Consideraciones Técnicas Específicas

### 4.1 Modelo de Usuario

El modelo de usuario para el módulo de registro debe implementar las siguientes consideraciones técnicas específicas que garantizan la compatibilidad con el framework Django y evitan conflictos con el modelo User nativo.

**Consideración técnica 1**: La clase de usuario debe llamarse YogaCenterUser para evitar conflictos con el modelo User nativo de Django. Esta convención de nomenclatura es crítica ya que la palabra "user" está reservada en Django y su uso podría generar conflictos graves en el sistema.

**Consideración técnica 2**: El modelo debe heredar de AbstractUser para reutilizar los atributos estándar (first_name, second_name, email, password, username) sin necesidad de redefinirlos. Esto garantiza la compatibilidad con el sistema de autenticación de Django y facilita la implementación de funcionalidades adicionales.

**Consideración técnica 3**: El nombre de los atributos del modelo debe seguir snake_case (por ejemplo: phone_number, first_name, date_of_birth) mientras que los nombres de las clases deben seguir CapWords (por ejemplo: YogaCenterUser, YogaCenterRole).

### 4.2 Atributos Adicionales del Modelo

Además de los atributos heredados de AbstractUser, el modelo debe incluir los siguientes atributos específicos para el caso de uso de registro:

| Atributo | Tipo | Descripción | Restricciones |
|----------|------|-------------|---------------|
| phone | CharField | Número de teléfono del usuario | Formato internacional, máximo 20 caracteres |
| date_of_birth | DateField | Fecha de nacimiento del usuario | Requerido para validación de edad |
| center | ForeignKey | Referencia al centro de yoga asociado | No puede ser nulo |
| role | ForeignKey | Rol asignado al usuario | No puede ser nulo |
| url_profile | ImageField | URL de la foto de perfil | Opcional |
| is_active | BooleanField | Estado de la cuenta | Valor por defecto: True |
| created_at | DateTimeField | Fecha de creación del registro | Auto-generado |

### 4.3 Validaciones Personalizadas

El modelo debe implementar las siguientes validaciones personalizadas para garantizar la integridad de los datos y el cumplimiento de los requisitos del caso de uso.

**Validación de correo electrónico único**: Antes de crear un usuario, el sistema debe verificar que el correo electrónico proporcionado no exista previamente en la base de datos. Esta validación debe realizarse tanto a nivel de formulario como a nivel de modelo para garantizar la integridad de los datos.

**Validación de edad mínima**: El sistema debe calcular la edad del usuario basándose en la fecha de nacimiento proporcionada y compararla con la edad mínima requerida por el centro de yoga. Si el usuario no cumple con este requisito, el registro debe ser rechazado con un mensaje apropiado.

**Validación de teléfono**: El número de teléfono debe seguir un formato internacional válido. Se recomienda el uso de bibliotecas especializadas para la validación de números de teléfono.

---

## 5. Implementación Técnica

### 5.1 Estructura del Modelo

El modelo YogaCenterUser debe implementarse siguiendo las convenciones establecidas y garantizando la compatibilidad con el sistema de autenticación de Django. A continuación, se presenta la estructura recomendada para el modelo.

```python
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone

class YogaCenterUser(AbstractUser):
    """
    Modelo personalizado de usuario para YogaCenter.
    Hereda de AbstractUser para reutilizar atributos estándar.
    """
    phone = models.CharField(
        max_length=20,
        blank=False,
        null=False,
        help_text="Número de teléfono con código internacional"
    )
    
    date_of_birth = models.DateField(
        blank=False,
        null=False,
        help_text="Fecha de nacimiento para verificación de edad"
    )
    
    center = models.ForeignKey(
        'YogaCenter',
        on_delete=models.CASCADE,
        related_name='users',
        help_text="Centro de yoga asociado al usuario"
    )
    
    role = models.ForeignKey(
        'YogaCenterRole',
        on_delete=models.PROTECT,
        related_name='users',
        help_text="Rol asignado al usuario"
    )
    
    url_profile = models.ImageField(
        upload_to='profiles/',
        null=True,
        blank=True,
        help_text="Foto de perfil del usuario"
    )
    
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Fecha de creación del registro"
    )
    
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="Fecha de última actualización"
    )
    
    class Meta:
        verbose_name = "Yoga Center User"
        verbose_name_plural = "Yoga Center Users"
        db_table = 'yoga_center_user'
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"
    
    def get_age(self):
        """Calcula la edad del usuario basándose en la fecha de nacimiento."""
        today = timezone.now().date()
        age = today.year - self.date_of_birth.year
        if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
            age -= 1
        return age
    
    def meets_age_requirement(self, minimum_age):
        """Verifica si el usuario cumple con la edad mínima requerida."""
        return self.get_age() >= minimum_age
```

### 5.2 Configuración del Modelo en Settings

Para que Django utilice el modelo personalizado, es necesario configurar la opción AUTH_USER_MODEL en el archivo de configuración settings.py. Esta configuración debe realizarse antes de cualquier migración y no debe cambiarse una vez que la aplicación está en producción.

```python
# En settings.py
AUTH_USER_MODEL = 'users.YogaCenterUser'
```

Es importante destacar que esta configuración debe ser realizada una única vez al inicio del proyecto y no debe modificarse posteriormente, ya que cambiar AUTH_USER_MODEL después de crear migraciones puede generar problemas graves de integridad de datos.

### 5.3 Implementación de Transacciones

Todas las operaciones de creación de usuario deben ejecutarse dentro de transacciones de base de datos para garantizar la atomicidad y evitar problemas de concurrencia. La siguiente implementación demuestra el uso correcto de transacciones en Django.

```python
from django.db import transaction
from django.core.exceptions import ValidationError

def create_user_with_transaction(user_data, center_id, role_id):
    """
    Crea un nuevo usuario dentro de una transacción atómica.
    
    Args:
        user_data: Diccionario con los datos del usuario
        center_id: ID del centro de yoga
        role_id: ID del rol a asignar
    
    Returns:
        YogaCenterUser: El usuario creado
    
    Raises:
        ValidationError: Si los datos no son válidos
        IntegrityError: Si hay violaciones de integridad en la base de datos
    """
    try:
        with transaction.atomic():
            # Bloqueo selectivo para evitar race conditions
            center = YogaCenter.objects.select_for_update().get(id=center_id)
            role = YogaCenterRole.objects.select_for_update().get(id=role_id)
            
            # Verificar unicidad del correo
            if YogaCenterUser.objects.filter(email=user_data['email']).exists():
                raise ValidationError({
                    'email': 'Este correo electrónico ya está registrado.'
                })
            
            # Validar edad mínima
            date_of_birth = user_data['date_of_birth']
            age = (timezone.now().date() - date_of_birth).days // 365
            if age < center.minimum_age:
                raise ValidationError({
                    'date_of_birth': f'Debe tener al menos {center.minimum_age} años.'
                })
            
            # Crear el usuario
            user = YogaCenterUser.objects.create_user(
                username=user_data['email'],
                email=user_data['email'],
                password=user_data['password'],
                first_name=user_data['first_name'],
                last_name=user_data['last_name'],
                phone=user_data['phone'],
                date_of_birth=date_of_birth,
                center=center,
                role=role,
                **user_data
            )
            
            return user
            
    except ValidationError as e:
        # Re-lanzar validaciones para manejo en el formulario
        raise e
    except Exception as e:
        # Log del error para debugging
        logger.error(f"Error al crear usuario: {e}")
        raise
```

---

## 6. Pruebas de Verificación

### 6.1 Prueba de Creación de Usuario

Esta prueba verifica que la creación de usuarios funciona correctamente y que los atributos se asignan apropiadamente.

```python
def test_create_user_success():
    """
    Prueba que se puede crear un usuario exitosamente.
    """
    # Configuración de datos de prueba
    center = YogaCenter.objects.create(
        name="Yoga Center Principal",
        address="Calle Principal 123",
        minimum_age=18
    )
    
    role = YogaCenterRole.objects.create(
        name="Yogui",
        description="Usuario regular del centro de yoga"
    )
    
    # Crear usuario de prueba
    user = YogaCenterUser.objects.create_user(
        username="test_user",
        password="secure_password_123",
        email="test@yoga.com",
        first_name="Juan",
        last_name="Pérez",
        phone="+584121234567",
        date_of_birth=timezone.now().date() - timedelta(days=7300),  # ~20 años
        center=center,
        role=role
    )
    
    # Verificaciones
    assert user.id is not None, "El usuario debe tener un ID asignado"
    assert user.phone == "+584121234567", "El teléfono debe coincidir"
    assert user.email == "test@yoga.com", "El correo debe coincidir"
    assert user.check_password("secure_password_123"), "La contraseña debe verificarse"
    assert user.center == center, "El centro debe estar asignado"
    assert user.role == role, "El rol debe estar asignado"
    
    print("PRUEBA EXITOSA: Usuario creado correctamente")
```

### 6.2 Prueba de Integridad de Datos

Esta prueba verifica que el sistema impide la creación de usuarios con datos inválidos o referencias a entidades inexistentes, garantizando la integridad referencial de la base de datos.

```python
def test_prevent_orphan_user():
    """
    Prueba que se previene la creación de usuarios huérfanos
    (con referencias a entidades que no existen).
    """
    try:
        # Intentar crear usuario con centro inexistente
        YogaCenterUser.objects.create(
            username="orphan_user",
            password="password",
            email="orphan@test.com",
            first_name="Test",
            phone="+584121234567",
            date_of_birth=timezone.now().date(),
            center_id=99999,  # ID inexistente
            role_id=1
        )
        print("ERROR: Se permitió crear un usuario huérfano")
    except IntegrityError:
        print("PRUEBA EXITOSA: La base de datos impidió crear un usuario huérfano")
    except Exception as e:
        print(f"Ocurrió otro error: {e}")
```

---

## 7. Relación con Otros Casos de Uso

### 7.1 Inclusión con Y1 (Ubicar Centro)

El caso de uso Y2 requiere que el usuario haya completado el caso de uso Y1 (Ubicar Centro) como precondición. Esta relación de inclusión garantiza que cada usuario registrado esté asociado con un centro de yoga específico, lo cual es fundamental para el funcionamiento del sistema.

La implementación técnica de esta relación incluye:

- El formulario de registro debe incluir un selector de centro basado en los resultados de Y1.
- Si el usuario no ha completado Y1, debe ser redirigido automáticamente.
- El centro seleccionado en Y1 debe persistir durante el proceso de registro.

### 7.2 Extensión hacia Y3 (Iniciar Sesión)

Después de un registro exitoso, el usuario debe ser redirigido al caso de uso Y3 (Iniciar Sesión). Esta extensión garantiza que el usuario pueda acceder a su cuenta inmediatamente después de registrarse, proporcionando una experiencia de usuario fluida y coherente.

La implementación técnica de esta extensión incluye:

- Redirección automática a la página de inicio de sesión.
- Mensaje de confirmación de registro exitoso.
- Generación de sesión automática (opcional) para mejorar la experiencia de usuario.

---

## 8. Referencias

- PEP 8: https://peps.python.org/pep-0008/
- Documentación oficial de Django: https://docs.djangoproject.com/es/6.0/
- Conventional Commits: https://www.conventionalcommits.org/en/v1.0.0/
- Django Transactions: https://docs.djangoproject.com/en/6.0/topics/db/transactions/
- Django Authentication: https://docs.djangoproject.com/en/6.0/topics/auth/

---

## 9. Control de Cambios

| Versión | Fecha | Descripción | Autor |
|---------|-------|-------------|-------|
| 1.0 | 2026-01-06 | Versión inicial del documento de caso de uso Y2 | MiniMax Agent |

---

## Anexo: Checklist de Implementación

Para garantizar el cumplimiento de todos los requisitos y estándares, el siguiente checklist debe ser revisado antes de considerar completada la implementación del caso de uso Y2.

- [ ] Modelo YogaCenterUser implementado heredando de AbstractUser
- [ ] AUTH_USER_MODEL configurado en settings.py
- [ ] Validación de correo electrónico único implementada
- [ ] Validación de edad mínima implementada
- [ ] Transacciones atómicas utilizadas en todas las operaciones de registro
- [ ] Pruebas unitarias creadas y passing
- [ ] Pruebas de integración creadas y passing
- [ ] Validación de referencias a entidades existentes implementada
- [ ] Integración con caso de uso Y1 verificada
- [ ] Integración con caso de uso Y3 implementada
- [ ] Mensajes de error claros y apropiados
- [ ] Documentación actualizada
- [ ] Commits siguiendo Conventional Commits
