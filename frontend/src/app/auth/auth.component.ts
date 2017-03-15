import { Component, OnInit } from '@angular/core';
import {AuthService} from "./auth.service";
import {Router} from "@angular/router";
// import { tokenNotExpired } from 'angular2-jwt';

@Component({
  selector: 'app-auth',
  templateUrl: './auth.component.html',
  styleUrls: ['./auth.component.css']
})
export class AuthComponent implements OnInit {
    title = "Lodin";
    email: string = "";
    password: string= "";
    headers: any;
    constructor(private _authService: AuthService, private _route: Router) { }

    logIn() {
      this._authService.logIn(this.email, this.password).subscribe(
            response => {
              localStorage.setItem('id_token', response.token);
              this._route.navigate(['/']);
            },
            error => console.log(error)
        );
    }
    ngOnInit() {
      console.log('in ngOnInit of Auth');
    }

}
