import { Component, OnInit } from '@angular/core';
import {AuthService} from "../auth.service";

@Component({
  selector: 'app-auth-signup',
  templateUrl: './auth-signup.component.html',
  styleUrls: ['./auth-signup.component.css']
})
export class AuthSignupComponent implements OnInit {
  email: string;
  password1: string;
  password2: string;
  error: string;

  constructor(private _authService: AuthService) { }

  signUp() {
    if(this.password1 !== this.password2) {
      this.error = "Passwords not equals.";
      return;
    }
    this._authService.signUp(this.email, this.password1).subscribe(
      response => localStorage.setItem('id_token', response.token),
      error => console.log(error)
    );
  }

  ngOnInit() {
  }

}
