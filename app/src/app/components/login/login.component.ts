import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrl: './login.component.css'
})
export class LoginComponent {
  // constructor(private http: HttpClient, private router: Router) {}

  // login(username: string, password: string) {
  //   // Aquí debes enviar los datos de inicio de sesión al backend
  //   const url = 'URL_DEL_BACKEND/login'; // Reemplaza 'URL_DEL_BACKEND' con la URL real del backend
  //   const body = { username, password }; // Datos a enviar al backend

  //   this.http.post<any>(url, body).subscribe(
  //     (response) => {
  //       // Si la respuesta es exitosa, puedes redirigir al usuario al home u otra página según sea necesario
  //       this.router.navigate(['/home']); // Reemplaza '/home' con la ruta real al home de tu aplicación
  //     },
  //     (error) => {
  //       // Si hay algún error en la respuesta del backend, puedes mostrar un mensaje de error al usuario o manejarlo de otra manera
  //       console.error('Error en la autenticación:', error);
  //     }
  //   );
  // }
}
