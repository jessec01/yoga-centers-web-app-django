# Tareas por completar (READMEN_TAREAS)

> Documento auxiliar para seguimiento. No reemplaza el README original.

## Pendientes críticos (Backend)
- [ ] Conectar endpoints reales de registro/login/verificación.
- [ ] Validación de email/teléfono con expiración de token.
- [ ] Rate limiting en endpoints sensibles.
- [ ] Políticas de contraseña y bloqueo por intentos.

## Pendientes de negocio
- [ ] Modelos de YogaCenter, Clase y Horario.
- [ ] CRUD básico para centros y clases.
- [ ] Página pública de centro.
- [ ] Listado y búsqueda por ubicación.

## Reservas y pagos
- [ ] Modelo de reservas y estados.
- [ ] Integración de pagos (Stripe u otro).
- [ ] Webhooks y reconciliación de estados.
- [ ] Políticas de cancelación y reembolso.

## Observabilidad y calidad
- [ ] Tests unitarios e integración.
- [ ] Logging estructurado y auditoría.
- [ ] Documentación de despliegue.

---

## Bibliografía (Backend)

### Autenticación, seguridad y JWT
- Django Security: https://docs.djangoproject.com/en/stable/topics/security/
- Django REST Framework Authentication: https://www.django-rest-framework.org/api-guide/authentication/
- JWT (RFC 7519): https://www.rfc-editor.org/rfc/rfc7519

### Arquitectura y API
- DRF API Guide: https://www.django-rest-framework.org/api-guide/
- OpenAPI Specification: https://spec.openapis.org/oas/latest.html

### Base de datos y rendimiento
- PostgreSQL Documentation: https://www.postgresql.org/docs/
- Django ORM Optimization: https://docs.djangoproject.com/en/stable/topics/db/optimization/

### Pagos y webhooks
- Stripe Docs: https://stripe.com/docs
- Webhook Best Practices: https://stripe.com/docs/webhooks

### Testing y calidad
- Django Testing: https://docs.djangoproject.com/en/stable/topics/testing/
- DRF Testing: https://www.django-rest-framework.org/api-guide/testing/

### Libros recomendados (backend)
- *Two Scoops of Django* — mejores prácticas para Django.
- *Django for APIs* — diseño de APIs con DRF.
- *Designing Data-Intensive Applications* — fundamentos de arquitectura backend.
