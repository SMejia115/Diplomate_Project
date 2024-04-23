import { Component, OnInit  } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { HttpClient } from '@angular/common/http';
import decodeToken from 'jwt-decode';

@Component({
  selector: 'app-shopping-cart',
  templateUrl: './shopping-cart.component.html',
  styleUrl: './shopping-cart.component.css'
})
export class ShoppingCartComponent implements OnInit{
  page!: string;
  title!: string;
  imageRoute!: string;
  productsCart: any;
  userID: any

  constructor(private route: ActivatedRoute, private http: HttpClient) { }

  ngOnInit(): void {
    this.route.params.subscribe(params => {
      this.page = params['page']; // Aquí obtienes el valor del parámetro de ruta
      console.log(this.page);
      this.title = 'Cart';
      this.imageRoute = '../../../assets/img/backgrounds/Background4.jpg';
    });
    const token:any = localStorage.getItem('token');
    const tokenDesencripted:any  = decodeToken(token)
    this.userID = tokenDesencripted.user.userID;;
    this.http.get(`http://localhost:8000/cart/${this.userID}`).subscribe((data: any) => {
      this.productsCart = data;
    });
  }
}
