import { Component, OnInit  } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-shopping-cart',
  templateUrl: './shopping-cart.component.html',
  styleUrl: './shopping-cart.component.css'
})
export class ShoppingCartComponent implements OnInit{
  page!: string;
  title!: string;
  imageRoute!: string;

  constructor(private route: ActivatedRoute) { }

  ngOnInit(): void {
    this.route.params.subscribe(params => {
      this.page = params['page']; // Aquí obtienes el valor del parámetro de ruta
      console.log(this.page);
      this.title = 'Cart';
      this.imageRoute = '../../../assets/img/backgrounds/Background4.jpg';
    });
  }
}
