import { Router } from '@angular/router';
import { CanActivate } from '@angular/router';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})

export class TokenGuardLogin implements CanActivate {
  constructor(private router: Router) { }

   canActivate(): boolean {
    const token:any = localStorage.getItem('token')
    if(token === null){
        return true;
      } else {
        this.router.navigate(['./home/shop']);
        return false;
      }
  }
}