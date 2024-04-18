import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-product-card',
  templateUrl: './product-card.component.html',
  styleUrl: './product-card.component.css'
})
export class ProductCardComponent {
  
  constructor(private router:Router) {}

  showMore(){
    this.router.navigate(['/product/1']);
  }

}
