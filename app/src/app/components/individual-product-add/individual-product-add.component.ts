import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-individual-product-add',
  templateUrl: './individual-product-add.component.html',
  styleUrls: ['./individual-product-add.component.css']
})
export class IndividualProductAddComponent {
  selectedImage: any;
  previousImage: any;
  quantity: number = 1;
  product: any = {
    productName: '',
    description: '',
    price: 0,
    category: '',
    images: []
  };

  constructor() {}

  updateProductInfo() {
    // Implementa la lógica para agregar un nuevo producto a la base de datos
    console.log('Agregando producto:', this.product);
    // Llama a un servicio o método para agregar el producto
    // this.productService.addProduct(this.product).subscribe(response => {
    //   console.log('Producto agregado exitosamente:', response);
    // });
  }

  selectImage(image: any, event: MouseEvent) {
    // Implementa la lógica de selección de imágenes
  }

  setQuantity(quantity: number) {
    // Implementa la lógica para ajustar la cantidad del producto
  }

  handleFileInput(event: any) {
    // Implementa la lógica para manejar la entrada de archivos
  }

  clearProductData() {
    // Establece todas las propiedades del producto en valores vacíos o predeterminados
    this.product = {
      productName: '',
      description: '',
      price: 0,
      category: '',
      images: []
    };
  }
}