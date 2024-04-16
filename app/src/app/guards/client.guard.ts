import { Router } from '@angular/router';
import decodeToken from 'jwt-decode';
import { CanActivate } from '@angular/router';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})

export class TokenGuardClient implements CanActivate {
  constructor(private router: Router) { }

   canActivate(): boolean {
    const token:any = localStorage.getItem('token')
    if(token !== null){
      const tokenDesencripted:any  = decodeToken(token)
      if (tokenDesencripted.user.role === 'client') {
        return true;
      } else {
        this.router.navigate(['./home/shop']);
        return false;
      }
    } else {
      console.log('Non-client user');
      this.router.navigate(['./home/shop']);
      return false;
    }
  }
}