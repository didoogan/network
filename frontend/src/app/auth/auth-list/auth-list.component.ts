import { Component, OnInit } from '@angular/core';
import {AuthService} from "../auth.service";

@Component({
  selector: 'app-auth-list',
  templateUrl: './auth-list.component.html',
  styleUrls: ['./auth-list.component.css']
})
export class AuthListComponent implements OnInit {
  public userList: any;

  constructor(private _authService: AuthService) {
    this._authService.getUsers()
      .subscribe(
        response => this.userList = response,
        error => console.log(error)
      );
  }

  ngOnInit() {
    console.log('in AuthListComponent');
  }

}
