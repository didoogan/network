import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';

import { AppComponent } from './app.component';
// import { AuthComponent } from './auth/auth.component';
import {RouterModule} from "@angular/router";
import {AuthModule} from "./auth/auth.module";

@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    AuthModule,
    BrowserModule,
    FormsModule,
    HttpModule,
    RouterModule.forRoot([
      { path: "auth",  loadChildren: './auth/auth.module#AuthModule'}
    ])
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
