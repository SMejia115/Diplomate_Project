import { NgModule } from '@angular/core';
import { RouterModule, Routes, Router, NavigationEnd } from '@angular/router';
import { MainHomeComponent } from './components/main-home/main-home.component';
import { RegisterComponent } from './components/register/register.component';
import { RangeValueAccessor } from '@angular/forms';
import { LoginComponent } from './components/login/login.component';
import { IndividualProductComponent } from './components/individual-product/individual-product.component';
import { TokenGuardAdmin } from './guards/admin.guard';
import { TokenGuardClient } from './guards/client.guard';

const routes: Routes = [
  { path: '', component: MainHomeComponent },
  { path: 'home/:page', component: MainHomeComponent },
  { path: 'register', component: RegisterComponent },
  { path: 'login', component: LoginComponent},
  { path: 'product/:id', component: IndividualProductComponent}
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