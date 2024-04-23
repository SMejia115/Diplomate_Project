import { Component, Input } from '@angular/core';
import decodeToken from 'jwt-decode';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-shop-product',
  templateUrl: './shop-product.component.html',
  styleUrls: ['./shop-product.component.css']
})
export class ShopProductComponent {
  @Input() product: any;
  userID: any;

  constructor(private http: HttpClient) {}

  setQuantity(quantity: number) {
    this.getUserID(); // Obtener el ID de usuario
    const user_id = this.userID;
    if (this.product.quantity + quantity >= 1) {
      this.product.quantity = this.product.quantity + quantity;
      this.http.put<any>(`http://localhost:8000/cart/update/${user_id}/${this.product.productID}/${this.product.quantity}`, {})
      .subscribe(
        response => {
          console.log('Producto eliminado del carrito:', response);
          window.location.reload();
        },
        error => {
          console.error('Error al eliminar el producto del carrito:', error);
          // Aquí puedes mostrar un mensaje de error al usuario
        }
      );
    }
  }

  getUserID() {
    const token:any = localStorage.getItem('token');
    const tokenDesencripted:any = decodeToken(token)
    this.userID = tokenDesencripted.user.userID;
  }

  deleteCart() {
    this.getUserID(); // Obtener el ID de usuario
    const user_id = this.userID;
    const product_id = this.product.productID;
    this.http.put<any>(`http://localhost:8000/cart/remove/${user_id}/${product_id}`, {})
      .subscribe(
        response => {
          console.log('Producto eliminado del carrito:', response);
          window.location.reload();
        },
        error => {
          console.error('Error al eliminar el producto del carrito:', error);
          // Aquí puedes mostrar un mensaje de error al usuario
        }
      );
  }
}
