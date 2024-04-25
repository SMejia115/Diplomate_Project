import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-main-home',
  templateUrl: './main-home.component.html',
  styleUrls: ['./main-home.component.css']
})
export class MainHomeComponent implements OnInit {
  page!: string;
  title!: string;
  imageRoute!: string;
  products: any;
  allProducts: any;
  searchTerm: string = ''

  constructor(private route: ActivatedRoute, private http: HttpClient) { }

  ngOnInit(): void {
    

    this.route.params.subscribe(params => {
      this.page = params['page']; // Aquí obtienes el valor del parámetro de ruta
      console.log(this.page);
      

      if (this.page === 'shop') {
        this.title = 'Shop';
        this.imageRoute = '../../../assets/shop_home.jpg';
        this.http.get('http://localhost:8000/products').subscribe((data: any) => {
          console.log(data);  
          this.allProducts = data;
          this.products = data;
        });
      } else if (this.page === 'caps') {
        this.title = 'Gorras';
        this.imageRoute = '../../../assets/img/backgrounds/caps_home.png';
        this.http.get('http://localhost:8000/products/category/cap').subscribe((data: any) => {
          console.log(data);  
          this.allProducts = data;
          this.products = data;
        });
      } else if (this.page === 'watchs') {
        this.title = 'Relojes';
        this.imageRoute = '../../../assets/img/backgrounds/watchs_home.jpg';
        this.http.get('http://localhost:8000/products/category/clock').subscribe((data: any) => {
          console.log(data);  
          this.allProducts = data;
          this.products = data;
        });
      }
      else {
        this.title = 'Shop';
        this.imageRoute = '../../../assets/shop_home.jpg';
        this.http.get('http://localhost:8000/products').subscribe((data: any) => {
          console.log(data);  
          this.allProducts = data;
          this.products = data;
        });
      }
    });
  }

  filterProducts(event: any): void {
    this.searchTerm = event.target.value;
    console.log(event.target.value)
    if (!this.searchTerm) {
      // Si el término de búsqueda está vacío, mostrar todos los productos
      this.products = this.allProducts;
    } else {
      // Filtrar los productos por nombre
      this.products = this.allProducts.filter((product: any) =>
        product.productName.toLowerCase().includes(this.searchTerm.toLowerCase())
      );
    }
  }
}