import { NgModule } from '@angular/core';
import { RouterModule, Routes, Router, NavigationEnd } from '@angular/router';
import { MainHomeComponent } from './components/main-home/main-home.component';
import { RegisterComponent } from './components/register/register.component';
import { RangeValueAccessor } from '@angular/forms';
import { LoginComponent } from './components/login/login.component';
import { IndividualProductComponent } from './components/individual-product/individual-product.component';
import { TokenGuardAdmin } from './guards/admin.guard';
import { TokenGuardClient } from './guards/client.guard';
import { TokenGuardLogin } from './guards/login.guard';
import { IndividualProductEditComponent } from './components/individual-product-edit/individual-product-edit.component';
import { ShoppingCartComponent } from './components/shopping-cart/shopping-cart.component';

const routes: Routes = [
  { path: '', component: MainHomeComponent },
  { path: 'home/:page', component: MainHomeComponent },
  { path: 'register', component: RegisterComponent, canActivate: [TokenGuardLogin]},
  { path: 'login', component: LoginComponent, canActivate: [TokenGuardLogin]},
  { path: 'product/:id', component: IndividualProductComponent},
  { path: 'edit/product/:id', component: IndividualProductEditComponent},
  { path: 'cart', component: ShoppingCartComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {
  constructor(private router: Router) {
    this.router.events.subscribe((event) => {
      if (event instanceof NavigationEnd) {
        window.scrollTo(0, 0); // Scrolls to the top of the page
      }
    });
  }
}