import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { MainHomeComponent } from './components/main-home/main-home.component';
import { RegisterComponent } from './components/register/register.component';
import { RangeValueAccessor } from '@angular/forms';
import { LoginComponent } from './components/login/login.component';
import { IndividualProductComponent } from './components/individual-product/individual-product.component';
import { TokenGuardAdmin } from './guards/admin.guard';
import { TokenGuardClient } from './guards/client.guard';
import { ShoppingCartComponent } from './components/shopping-cart/shopping-cart.component';

const routes: Routes = [
  { path: '', component: MainHomeComponent },
  { path: 'home/:page', component: MainHomeComponent },
  { path: 'register', component: RegisterComponent },
  { path: 'login', component: LoginComponent},
  { path: 'product/:id', component: IndividualProductComponent},
  { path: 'cart', component: ShoppingCartComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes, { onSameUrlNavigation: 'reload' })],
  exports: [RouterModule]
})
export class AppRoutingModule { }
