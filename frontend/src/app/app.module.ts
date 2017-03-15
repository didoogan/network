import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';

import { AppComponent } from './app.component';
// import { AuthComponent } from './auth/auth.component';
import {RouterModule} from "@angular/router";
import {AuthModule} from "./auth/auth.module";
import {PostModule} from "./post/post.module";

@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    AuthModule,
    PostModule,
    BrowserModule,
    FormsModule,
    HttpModule,
    RouterModule.forRoot([
      { path: "auth",  loadChildren: './auth/auth.module#AuthModule'},
      { path: "post",  loadChildren: './post/post.module#PostModule'},
      { path: "",  redirectTo: '/post/post-list', pathMatch: 'full'}
    ])
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
