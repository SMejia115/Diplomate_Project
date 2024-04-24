import { Component, OnInit, ViewChild, ViewEncapsulation } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { MatTableDataSource } from '@angular/material/table';
import { MatSort } from '@angular/material/sort';
import { MatPaginator } from '@angular/material/paginator';
import { Router } from '@angular/router';


@Component({
  selector: 'app-admin-home',
  templateUrl: './admin-home.component.html',
  styleUrl: './admin-home.component.css'
})
export class AdminHomeComponent implements OnInit{
  @ViewChild(MatSort) sort!: MatSort;
  @ViewChild(MatPaginator) paginator!: MatPaginator; // Añade ViewChild para el paginador

  allProducts: any
  products: any

  columns: String[] = ['ID', 'Nombre', 'Categoria', 'Cantidad', 'Precio', 'Accion']
  dataSource = new MatTableDataSource();

  constructor(private http: HttpClient, private router:Router){}

  ngOnInit(): void {
    this.getProducts();
  }

  getProducts(): void{
    this.http.get('http://localhost:8000/products').subscribe((data: any) => {
      console.log(data)
      this.allProducts = data;
      this.products = data;
      this.dataSource = new MatTableDataSource(data);
      this.dataSource.sort = this.sort;
      this.dataSource.paginator = this.paginator;
    });
  }

  applyFilter(event: Event) {
    const filterValue = (event.target as HTMLInputElement).value;
    this.dataSource.filter = filterValue.trim().toLowerCase();

    if (this.dataSource.paginator) {
      this.dataSource.paginator.firstPage();
    }
  }

  editProduct(product: any): void{
    this.router.navigate([`edit/product/${product.productID}`])
  }

  deleteProduct(product: any): void{
    console.log('Delete product', product)
  }

}
