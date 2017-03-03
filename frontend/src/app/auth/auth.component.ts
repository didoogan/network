import { Component, OnInit } from '@angular/core';
import {AuthService} from "./auth.service";

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
    constructor(private _authService: AuthService) { }

    logIn() {
      this._authService.logIn(this.email, this.password).subscribe(
            response => console.log(response),
            error => console.log(error)
        );
    }
    ngOnInit() {
      console.log('in ngOnInit of Auth');
    }

}
