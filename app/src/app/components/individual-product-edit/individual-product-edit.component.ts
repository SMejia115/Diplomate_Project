import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-individual-product-edit',
  templateUrl: './individual-product-edit.component.html',
  styleUrl: './individual-product-edit.component.css'
})
export class IndividualProductEditComponent {
 selectedImage: any;
 previousImage: any;
 quantity: number = 1;
 productID!: number;
 product!: any;

 constructor(private http: HttpClient, private route: ActivatedRoute){}

 ngOnInit(){
   console.log('Se inicializa la vista')
   this.route.params.subscribe(params => {
     this.productID = params['id']; // Aquí obtienes el valor del parámetro de ruta
     console.log(this.productID)
     this.http.get(`http://localhost:8000/products/${this.productID}`).subscribe((data: any) => {
       console.log(data);  
       this.product = data;
       this.selectedImage = this.product.images[0]
       console.log(this.selectImage)
     });
   });
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
