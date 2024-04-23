import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-shop-product',
  templateUrl: './shop-product.component.html',
  styleUrl: './shop-product.component.css'
})
export class ShopProductComponent {
  @Input() product: any;
  quantity: number = 1;
  
  setQuantity(quantity: number) {
    if (this.product.quantity+quantity >= 1){
      this.product.quantity = this.product.quantity+quantity;
    }
  }
}
