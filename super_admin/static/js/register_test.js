//experimental
document.addEventListener('DOMContentLoaded', function() {
    const button_save=document.getElementById('button-save');
   button_save.addEventListener('submit',function(event){
      event.preventDefault();
      //el method define si es post o get
      //content-type define el formato de los datos
      //body son los datos que se envian al servidor
      const formData={
         username: "testuser",
         password: "testpassword",
         email: "testuser@example.com",
         first_name: "Test",
         last_name: "User",
         phone: "1234567890"
      };
   fetch('/user/api/register/', {
         method: 'POST',
         headers: {
            'Content-Type': 'application/json',
            // NOTA: No enviamos token de autorización
            // porque este es un endpoint público (AllowAny)
            },
         body: JSON.stringify(formData) // Convertimos el objeto JS a JSON
    })
   .then(response => {
      if (!response.ok) {
         throw new Error('Network response was not ok ' + response.statusText);
         console.log('caso base los datos no se enviaron');
      }
      console.log('caso exito los datos se enviaron');
      return response.json(); // Parseamos la respuesta JSON
   })
   .then(data => {
      console.log('Success:', data);
      console.log('los datos se procesaron y fueron devueltos por el servidor con errores');
      // Aquí puedes manejar la respuesta del servidor
   })
   .catch((error) => {
      console.error('Error:', error);
      console.log('los datos no se enviaron por un error de red u otro problema');   
   });
   });
});