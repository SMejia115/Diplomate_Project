import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { MainHomeComponent } from './components/main-home/main-home.component';
import { RegisterComponent } from './components/register/register.component';
import { RangeValueAccessor } from '@angular/forms';
import { LoginComponent } from './components/login/login.component';
import { TokenGuardAdmin } from './guards/admin.guard';
import { TokenGuardClient } from './guards/client.guard';

const routes: Routes = [
  { path: '', component: MainHomeComponent },
  { path: 'home/:page', component: MainHomeComponent },
  { path: 'register', component: RegisterComponent},
  { path: 'login', component: LoginComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes, { onSameUrlNavigation: 'reload' })],
  exports: [RouterModule]
})
export class AppRoutingModule { }
