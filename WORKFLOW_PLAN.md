# Plan de trabajo diario (levantamiento del proyecto)

Este documento divide tareas por complejidad e investigación, con un orden sugerido para avanzar cada día.

> Nota: Este plan se apoya en los hallazgos de AUDIT_ROADMAP.md y prioriza backend.

---

## Fase 0 — Preparación (Día 1)
**Complejidad: Baja | Investigación: Baja**
1) Revisar variables de entorno y configuración base.
2) Confirmar migraciones y estado de la base de datos.
3) Verificar que Django y DRF están operativos.

**Entrega del día**
- Proyecto corre localmente y conecta a PostgreSQL.

---

## Fase 1 — Autenticación y seguridad básica (Días 2–4)
**Complejidad: Media | Investigación: Media**
1) Conectar endpoints reales de registro/login y verificación.
2) Validación de email/telefono y expiración de tokens.
3) Implementar rate limiting y políticas de contraseña.

**Entrega del día 2**
- Registro/Login funcional con validación server-side.

**Entrega del día 3**
- Verificación de email/telefono con expiración y reintentos controlados.

**Entrega del día 4**
- Seguridad mínima: rate limiting, logs de auditoría, protección CSRF en formularios.

---

## Fase 2 — Modelos base del negocio (Días 5–8)
**Complejidad: Media | Investigación: Media**
1) Crear modelos: YogaCenter, Clase, Horario.
2) CRUD básico para centros y clases.
3) Página pública de centro y lista de centros.

**Entrega del día 5**
- Modelos creados y migrados.

**Entrega del día 6**
- Endpoints CRUD para centros.

**Entrega del día 7**
- Endpoints CRUD para clases y horarios.

**Entrega del día 8**
- Plantilla pública para centro + listado con filtros básicos.

---

## Fase 3 — Reservas (Días 9–12)
**Complejidad: Alta | Investigación: Media**
1) Modelo de Reserva y reglas de capacidad.
2) Endpoints de creación y cancelación.
3) Políticas de cancelación y estados.

**Entrega del día 9**
- Modelo de reservas y estados definido.

**Entrega del día 10**
- Endpoints creación/cancelación funcionando.

**Entrega del día 11**
- Políticas de cancelación aplicadas.

**Entrega del día 12**
- Notificación básica (email) al crear/cancelar.

---

## Fase 4 — Pagos (Días 13–16)
**Complejidad: Alta | Investigación: Alta**
1) Integración de pagos (Stripe u otro).
2) Webhooks y reconciliación de estados.
3) Manejo de errores y reintentos.

**Entrega del día 13**
- Flujo de cobro en sandbox.

**Entrega del día 14**
- Webhooks con actualización de estado.

**Entrega del día 15**
- Políticas de reembolso básicas.

**Entrega del día 16**
- Registro de pagos y auditoría.

---

## Fase 5 — Reputación y mensajería (Días 17–20)
**Complejidad: Media | Investigación: Media**
1) Reseñas y calificaciones.
2) Mensajería entre usuario y centro.
3) Moderación básica.

---

## Fase 6 — Observabilidad y calidad (Días 21–24)
**Complejidad: Media | Investigación: Media**
1) Tests unitarios/integración/e2e para flujos críticos.
2) Logging estructurado y métricas.
3) Backups y documentación de despliegue.

---

## Reglas de priorización (para cada día)
1) Seguridad y autenticación primero.
2) Modelos de negocio antes de UI avanzada.
3) Flujo completo (end-to-end) antes de optimizaciones.
