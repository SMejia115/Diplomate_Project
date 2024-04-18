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
          this.products = data;
        });
      } else if (this.page === 'caps') {
        this.title = 'Gorras';
        this.imageRoute = '../../../assets/img/backgrounds/caps_home.png';
      } else if (this.page === 'watchs') {
        this.title = 'Relojes';
        this.imageRoute = '../../../assets/img/backgrounds/watchs_home.jpg';
      }
    });
  }
}