import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'Home';
  email: string = "";
  password: string= "";

  constructor() { }

  onSubmit() {
    console.log(this.email);
    console.log(this.password);
  }
}
