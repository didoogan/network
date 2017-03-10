import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import {AuthComponent} from "./auth.component";

import { Http, RequestOptions } from '@angular/http';
import { AuthHttp, AuthConfig } from 'angular2-jwt';
import {AuthService} from "./auth.service";
import {RouterModule} from "@angular/router";
import {FormsModule} from "@angular/forms";
import { AuthListComponent } from './auth-list/auth-list.component';
import { AuthSignupComponent } from './auth-signup/auth-signup.component';

function authHttpServiceFactory(http: Http, options: RequestOptions) {
  return new AuthHttp(new AuthConfig(), http, options);
}

@NgModule({
  imports: [
    FormsModule,
    CommonModule,
    RouterModule.forChild([
      { path: "login", component: AuthComponent },
      { path: "signup", component: AuthSignupComponent },
      {path: "user-list", component: AuthListComponent}
    ])
  ],
  declarations: [AuthComponent, AuthListComponent, AuthSignupComponent],
  providers: [
    {
      provide: AuthHttp,
      useFactory: authHttpServiceFactory,
      deps: [Http, RequestOptions]
    },
    AuthService
  ]
})
export class AuthModule { }
