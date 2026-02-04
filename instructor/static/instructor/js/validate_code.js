/* validate_code.js
   - Implementa un temporizador de 60 segundos para la verificación del código.
   - Gestiona la habilitación del botón de 'Reenviar código' cuando el temporizador llega a 0.

   Comentarios importantes (qué debe hacer el frontend/backend):
   - El backend debe imponer rate-limits y TTL del código; el frontend solo muestra estado.
   - Para mejorar UX, mostrar mensajes inline de error/success y bloquear inputs durante la validación.
   - Reenviar código debe llamar a un endpoint que genere y envíe otro código; el backend decide política.

   Código activo aquí: temporizador y control de reenvío (pequeño y seguro, no envía peticiones automáticas).
*/

document.addEventListener('DOMContentLoaded', function(){
  const countdownEl = document.getElementById('countdown');
  const resendBtn = document.getElementById('resend-btn');
  const CODE_TTL = 60; // segundos
  let remaining = CODE_TTL;
  let timerId = null;

  function formatTime(s){
    const mm = String(Math.floor(s/60)).padStart(2,'0');
    const ss = String(s%60).padStart(2,'0');
    return `${mm}:${ss}`;
  }

  function tick(){
    remaining -= 1;
    if(remaining < 0){
      clearInterval(timerId);
      countdownEl.textContent = formatTime(0);
      resendBtn.disabled = false;
      return;
    }
    countdownEl.textContent = formatTime(remaining);
  }

  // iniciar temporizador
  countdownEl.textContent = formatTime(remaining);
  resendBtn.disabled = true;
  timerId = setInterval(tick, 1000);

  // si el usuario pulsa reenviar, se debe llamar a un endpoint (no lo implementamos aquí)
  resendBtn.addEventListener('click', function(){
    // Comentario: aquí debes implementar la llamada fetch POST a tu endpoint de reenvío
    // Ejemplo (no ejecutado):
    // fetch('/instructor/api/resend-code/', { method: 'POST', headers:{'X-CSRFToken':...} })
    //   .then(resp => { /* manejar respuesta y reiniciar temporizador si procede */ })

    // Mientras tanto, reiniciamos visualmente el temporizador y deshabilitamos el botón
    remaining = CODE_TTL;
    resendBtn.disabled = true;
    clearInterval(timerId);
    timerId = setInterval(tick, 1000);
  });

  // Validación simple en envío: asegurar patrón de 6 dígitos antes de enviar al servidor
  const form = document.getElementById('validate-form');
  if(form){
    form.addEventListener('submit', function(e){
      const codeInput = document.getElementById('code-input');
      const val = codeInput && codeInput.value ? codeInput.value.trim() : '';
      if(!/^\d{6}$/.test(val)){
        e.preventDefault();
        codeInput.focus();
        // Aquí se podría mostrar un mensaje inline; mantener minimalista por ahora.
      }
      // Nota: la validación definitiva debe hacerse en servidor.
    });
  }
});
