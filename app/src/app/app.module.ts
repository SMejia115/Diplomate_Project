import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { ReactiveFormsModule } from '@angular/forms'; // Importa ReactiveFormsModule

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HeaderComponent } from './components/header/header.component';
import { LoginComponent } from './components/login/login.component';
import { FormsModule } from '@angular/forms';
import { MainHomeComponent } from './components/main-home/main-home.component';
import { ProductCardComponent } from './components/product-card/product-card.component';
import { FooterComponent } from './components/footer/footer.component';
import { RegisterComponent } from './components/register/register.component';
import { IndividualProductComponent } from './components/individual-product/individual-product.component';
import { HttpClientModule } from '@angular/common/http';
import { IndividualProductEditComponent } from './components/individual-product-edit/individual-product-edit.component';
import { ShoppingCartComponent } from './components/shopping-cart/shopping-cart.component';
import { ShopProductComponent } from './components/shop-product/shop-product.component';


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
    ShoppingCartComponent,
    ShopProductComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    ReactiveFormsModule,
    FormsModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
