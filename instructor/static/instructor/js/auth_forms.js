/* auth_forms.js
   Archivo genérico para manejar formularios de autenticación (registro + login)

   Contenido:
   - Comentarios detallados sobre qué implica combinar registro y login en una sola plantilla.
   - Lógica pequeña y no intrusiva permitida: mostrar/ocultar contraseñas y alternar vistas
     (registro/login) usando el hash de la URL (#register / #login) o botones internos.
   - NOTA: Validaciones avanzadas, envío AJAX y manejo seguro de tokens deben implementarse
     en archivos separados o en el backend. Aquí sólo hay lógica de presentación.

   Uso: incluir {% static 'instructor/js/auth_forms.js' %} en plantillas que usen ambos formularios.
*/

document.addEventListener('DOMContentLoaded', function(){
  // --- Comentarios sobre la arquitectura ---
  // 1) Esta biblioteca asume que ambos formularios (registro y login) viven en la misma
  //    plantilla y tienen ids: 'register-form' y 'login-form'. Si cambias esos ids,
  //    actualiza las referencias aquí o inicialízalo desde tu código.
  // 2) La lógica de presentación (mostrar/ocultar) se realiza en el cliente y NO
  //    sustituye las validaciones ni la seguridad del servidor. Todas las comprobaciones
  //    sensibles (tokens, límites de intentos, verificación de email) deben manejarse
  //    en el backend.
  // 3) Mantén el degradado sin JS: los formularios deben poder enviarse por POST.

  // --- Helpers: mostrar/ocultar contraseña ---
  function bindShowPassword(pwSelector, cbSelector){
    const pw = document.getElementById(pwSelector);
    const cb = document.getElementById(cbSelector);
    if(pw && cb){
      cb.addEventListener('change', function(){
        pw.type = cb.checked ? 'text' : 'password';
      });
    }
  }
  // Bind para los controles típicos usados en las plantillas
  bindShowPassword('password','show-password');
  bindShowPassword('login-password','show-password-login');

  // --- Alternar vistas (registro / login) ---
  // Permite tener una sola plantilla y mostrar el formulario apropiado según la hash
  // de la URL. También facilita enlaces internos que apuntan a #login o #register.
  const registerForm = document.getElementById('register-form');
  const loginForm = document.getElementById('login-form');

  function showViewFromHash(){
    const h = window.location.hash || '#register';
    if(h === '#login'){
      if(registerForm) registerForm.style.display = 'none';
      if(loginForm) loginForm.style.display = 'block';
    }else{
      if(loginForm) loginForm.style.display = 'none';
      if(registerForm) registerForm.style.display = 'block';
    }
  }
  window.addEventListener('hashchange', showViewFromHash);
  showViewFromHash();

  // --- Comentarios sobre mejoras potenciales ---
  // - Persistir la vista seleccionada en localStorage si se desea recordar la preferencia.
  // - Añadir transiciones suaves (CSS) al mostrar/ocultar formularios para mejor UX.
  // - Implementar validación progresiva y manejo de errores en JS; siempre repetir en servidor.
  // - Si se agrega envío AJAX, centralizar lógica de petición y manejo de CSRF.
  // - Al combinar ambos formularios en una sola plantilla, mantener IDs y nombres únicos
  //   para campos que puedan colisionar (por ejemplo 'username' aparece en ambos: esto está bien
  //   si los formularios no se envían simultáneamente; pero en JS es útil seleccionar por
  //   `#register-form [name=username]` para evitar ambigüedades).

});
