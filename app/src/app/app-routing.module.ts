import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { MainHomeComponent } from './components/main-home/main-home.component';

const routes: Routes = [
  { path: '', component: MainHomeComponent },
  { path: 'home/:page', component: MainHomeComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes, { onSameUrlNavigation: 'reload' })],
  exports: [RouterModule]
})
export class AppRoutingModule { }
