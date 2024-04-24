import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { ReactiveFormsModule } from '@angular/forms'; // Importa ReactiveFormsModule
import { MatTableModule } from '@angular/material/table';
import { MatSortModule } from '@angular/material/sort';
import { MatPaginatorModule } from '@angular/material/paginator';
import { MatIconModule } from '@angular/material/icon';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HeaderComponent } from './components/header/header.component';
import { LoginComponent } from './components/login/login.component';
import { AboutComponent } from './components/about/about.component';
import { FormsModule } from '@angular/forms';
import { MainHomeComponent } from './components/main-home/main-home.component';
import { ProductCardComponent } from './components/product-card/product-card.component';
import { FooterComponent } from './components/footer/footer.component';
import { RegisterComponent } from './components/register/register.component';
import { IndividualProductComponent } from './components/individual-product/individual-product.component';
import { HttpClientModule } from '@angular/common/http';
import { IndividualProductEditComponent } from './components/individual-product-edit/individual-product-edit.component';
import { IndividualProductAddComponent } from './components/individual-product-add/individual-product-add.component';
import { ShoppingCartComponent } from './components/shopping-cart/shopping-cart.component';
import { ShopProductComponent } from './components/shop-product/shop-product.component';
import { AdminHomeComponent } from './components/admin-home/admin-home.component';
import { provideAnimationsAsync } from '@angular/platform-browser/animations/async';
import { AboutUsComponent } from './components/about-us/about-us.component';


@NgModule({
  declarations: [
    AppComponent,
    HeaderComponent,
    LoginComponent,
    MainHomeComponent,
    ProductCardComponent,
    FooterComponent,
    RegisterComponent,
    IndividualProductComponent,
    IndividualProductEditComponent,
    IndividualProductAddComponent,
    ShoppingCartComponent,
    AboutComponent,
    ShopProductComponent,
    AdminHomeComponent,
    AboutUsComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    ReactiveFormsModule,
    FormsModule,
    HttpClientModule,
    MatTableModule,
    MatSortModule,
    MatPaginatorModule,
    MatIconModule
  ],
  providers: [
    provideAnimationsAsync()
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
