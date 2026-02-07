/* auth_form.js (center_administrator)
   Adaptado desde instructor/js/auth_forms.js para usar con la app center_administrator.

   Responsabilidades (ligeras):
   - Mostrar/ocultar contraseñas
   - Alternar vista registro/login usando hash de URL (#register / #login)
   - Dejar la experiencia usable sin JS (degradado)

   NOTA: validaciones sensibles, envío AJAX y seguridad deben implementarse en el
   backend o en módulos separados que manejen CSRF/errores.
*/

document.addEventListener('DOMContentLoaded', function(){
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

  // Campos usados en la plantilla de center_administrator (IDs compatibles)
  bindShowPassword('password','show-password');
  bindShowPassword('login-password','show-password-login');

  // --- Alternar vistas (registro / login) ---
  const registerForm = document.getElementById('register-form');
  const loginForm = document.getElementById('login-form');

  function showViewFromHash(){
    const h = window.location.hash || '#register';
    if(h === '#login'){
      if(registerForm) registerForm.style.display = 'none';
      if(loginForm) loginForm.style.display = 'block';
    } else {
      if(loginForm) loginForm.style.display = 'none';
      if(registerForm) registerForm.style.display = 'block';
    }
  }
  window.addEventListener('hashchange', showViewFromHash);
  showViewFromHash();

  // --- Mejora UX: enlaces internos que alternan vistas ---
  const toLogin = document.getElementById('to-login');
  const toRegister = document.getElementById('to-register');
  if(toLogin) toLogin.addEventListener('click', function(){ window.location.hash = '#login'; });
  if(toRegister) toRegister.addEventListener('click', function(){ window.location.hash = '#register'; });

  // --- Comentarios y extensiones posibles ---
  // - Si se añade envío AJAX, centralizar aquí el manejo de fetch + CSRF.
  // - Para accesibilidad, gestionar focus cuando se cambia de vista.
  // - Mantener nombres/IDs consistentes entre plantillas y este archivo.
});
