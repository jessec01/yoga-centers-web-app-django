/* main.js - placeholder con ideas de mejoras JS (no requerido para funcionamiento sin JS)

  Sugerencias de qué añadir aquí (comentadas):
  - Mejora progresiva: detectar si el navegador soporta JS y añadir pequeñas mejoras UX.
  - Validación de formularios antes de enviar (por ejemplo, comprobar campos obligatorios).
  - Mejores transiciones y accesibilidad (focus management al abrir modales).
  - Carga perezosa de imágenes y tracking (analytics) event-based.
  - Implementar modales o formularios embebidos con degradado a enlaces normales si JS no está presente.

  NOTA: Los botones de registro/login en la plantilla están hechos para funcionar sin JS.
  Este archivo es solo un punto de partida con ideas y hooks para enlazar.

*/

// Ejemplo mínimo: marcar en el DOM si hay JS disponible
(function(){
  try{
    document.documentElement.classList.add('has-js');
  }catch(e){
    // entorno sin DOM disponible o protegido
  }
})();

/*
  Aquí puede ir:
  - hooks para mejorar accesibilidad (ej. cerrar modales con ESC)
  - funciones para validar datos del lado cliente
  - init de analítica (si aplica)

  Recuerda no depender de JS para el flujo principal (registro/login).
*/
