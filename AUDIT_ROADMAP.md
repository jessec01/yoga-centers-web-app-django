# Auditoría y Roadmap — Yoga Centers Web App (Django)

Documento auxiliar (no reemplaza README.md). Estado al 3 de febrero de 2026.

---

## 1) Estado actual del proyecto (resumen ejecutivo)

- **Stack**: Django + Django REST Framework + PostgreSQL.
- **Apps detectadas** (según configuración):
  - `yogacenterwebapp` (core/proyecto y configuración)
  - `userYC` (usuario principal del sistema)
  - `yogui` (perfil/rol de usuario yogui)
  - `instructor` (registro/login y vistas relacionadas para instructores)
  - `center_administrator` (administración de centros)
  - `super_admin` (panel/funciones de super administrador)
  - `magiclink` (tokens y enlaces mágicos por email)

- **Frontend** (estado actual):
  - Formularios con diseño minimalista “Zen” y paleta relajante.
  - Plantilla genérica `auth_form.html` que combina **registro + login**.
  - Scripts compartidos para **modo oscuro** (`yogacenterwebapp/js/theme.js`).
  - Script genérico para formularios de autenticación (`instructor/js/auth_forms.js`).

- **Autenticación**:
  - JWT configurado en `settings.py` (access/refresh tokens).
  - Token mágico en `magiclink` (presente; falta verificación de flujo completo).

- **Base de datos**:
  - PostgreSQL configurado por variables de entorno.

---

## 2) Auditoría del estado (completa y accionable)

> Esta auditoría se basa en la estructura detectada y configuración presente. Algunas áreas requieren verificación en ejecución y pruebas end-to-end.

### 2.1 Arquitectura y modularidad
- ✅ Separación por apps (roles y dominios bien diferenciados).
- ✅ `settings.py` limpio para JWT y DRF.
- ⚠️ Recomendada consolidación de **nomenclaturas** y rutas de templates/endpoints.

### 2.2 Autenticación y seguridad
- ✅ JWT configurado.
- ⚠️ Verificar expiraciones reales, refresco y rotación de tokens.
- ⚠️ Falta rate limiting en endpoints críticos.
- ⚠️ Recomendado: políticas de contraseñas, lockout por intentos y logs de auditoría.

### 2.3 Flujos de usuario
- ✅ Templates para **registro/login** y **verificación de código**.
- ⚠️ Falta flujo de onboarding completo (perfil, completar datos, activar cuenta, etc.).

### 2.4 UX/UI
- ✅ Estilo minimalista y consistente (Zen).
- ✅ Modo oscuro compartido.
- ⚠️ Faltan páginas públicas finales y feedback de errores/success en formularios.

### 2.5 API y servicios
- ✅ DRF instalado y base para endpoints.
- ⚠️ Faltan contratos API documentados (OpenAPI/Swagger).
- ⚠️ Faltan endpoints clave (catálogo, reservas, pagos, reseñas).

### 2.6 Datos y modelos
- ✅ Módulos de usuarios y perfiles presentes.
- ⚠️ Falta definir modelos de negocio completos (centros, clases, horarios, reservas, pagos).

### 2.7 Testing
- ✅ Existen tests de ejemplo.
- ⚠️ Faltan suites completas: unit, integración y e2e de flujos críticos.

### 2.8 Operaciones y despliegue
- ✅ Dockerfile y docker-compose presentes.
- ⚠️ Falta documentación de despliegue (entornos, variables, migraciones, backups).

---

## 3) Requerimientos futuros (por app) y orden recomendado

> Objetivo: permitir que empresas de yoga registren su negocio, publiquen servicios y reciban clientes desde la plataforma.

### 3.1 Fase 1 — Fundamentos de autenticación y perfiles (alta)
**Apps**: `userYC`, `yogui`, `instructor`, `magiclink`
1) Unificar registro/login en `auth_form.html` y conectar endpoints reales. ✅ (UI) / ⚠️ (backend)
2) Validación robusta de email/teléfono y verificación de cuenta (token/email).
3) Perfil básico de instructor/empresa (datos mínimos: nombre comercial, ciudad, contacto).
4) Reglas de seguridad y rate limiting para endpoints críticos.

### 3.2 Fase 2 — Núcleo de negocio (alta)
**Apps**: `center_administrator`, `instructor`, `userYC`
1) Modelo de **YogaCenter** (ubicación, servicios, horarios).
2) CRUD de clases y horarios (instructor/centro).
3) Página pública del centro (perfil, clases, contacto).
4) Búsqueda/listado de centros por ubicación y filtro.

### 3.3 Fase 3 — Reservas y pagos (media)
**Apps**: `yogui`, `userYC`, `center_administrator`
1) Modelo de **Reserva** (estado, cancelaciones, cupos).
2) Integración de pago (Stripe o similar).
3) Políticas de cancelación y reembolso.

### 3.4 Fase 4 — Reputación y crecimiento (media)
**Apps**: `yogui`, `center_administrator`
1) Reseñas y calificaciones.
2) Sistema de mensajes entre usuario y centro.
3) Panel de métricas para centros (reservas, conversiones, ingresos).

### 3.5 Fase 5 — Escalabilidad y operaciones (media-baja)
1) Auditoría de seguridad formal.
2) Monitorización y logging centralizado.
3) Backups automáticos y observabilidad.

---

## 4) Recomendaciones inmediatas (7–14 días)

1) **Normalizar rutas y templates**: asegurar que todas las vistas apunten a `auth_form.html`.
2) **Completar flujo de verificación de email** con token válido y expiración.
3) **Crear modelos base de negocio** (YogaCenter, Clase, Horario) y endpoints mínimos.
4) **Definir contrato API** (OpenAPI/Swagger) para frontend y QA.

---

## 5) Notas

- Este documento es un complemento del README.
- Si necesitas auditoría con métricas reales (tests, cobertura, rendimiento), ejecutar pruebas y anexar resultados.
