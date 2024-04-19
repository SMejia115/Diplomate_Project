import { Component } from '@angular/core';

@Component({
  selector: 'app-shop-product',
  templateUrl: './shop-product.component.html',
  styleUrl: './shop-product.component.css'
})
export class ShopProductComponent {
  quantity: number = 1;
  
  setQuantity(quantity: number) {
    if (this.quantity+quantity >= 1){
      this.quantity = this.quantity+quantity;
    }
  }
}
