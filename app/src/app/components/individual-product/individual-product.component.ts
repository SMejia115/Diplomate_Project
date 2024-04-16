import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-individual-product',
  templateUrl: './individual-product.component.html',
  styleUrl: './individual-product.component.css'
})
export class IndividualProductComponent implements OnInit{
  images = [
    {url: '../../../assets/img/products/Gorra1.png'},
    {url: '../../../assets/img/products/Gorra2.png'},
    {url: '../../../assets/img/products/Gorra1.png'},
    {url: '../../../assets/img/products/Gorra2.png'}
  ]
  selectedImage: any;
  previousImage: any;
  quantity: number = 1;

  ngOnInit(){
    this.selectedImage = this.images[0];
  }

  selectImage(image: any, event: MouseEvent) {
    if (event.type === 'click') {
      // Si el evento es un clic, simplemente establece la imagen seleccionada
      this.selectedImage = image;
    } else if (event.type === 'mouseenter') {
      // Si el evento es hover, guarda la imagen actual y establece la nueva imagen seleccionada
      this.previousImage = this.selectedImage;
      this.selectedImage = image;
    } else if (event.type === 'mouseleave') {
      // Si el evento es hover y el mouse deja la imagen, restaura la imagen principal anterior
      this.selectedImage = this.previousImage;
    }
  }

  setQuantity(quantity: number) {
    if (this.quantity+quantity >= 1){
      this.quantity = this.quantity+quantity;
    }
  }

}
