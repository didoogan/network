import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent  implements OnInit{
  title = 'Home';
  email: string = "";
  password: string= "";

  constructor() { }

  onSubmit() {
    console.log(this.email);
    console.log(this.password);
  }
  ngOnInit() {
    console.log('in ngOninit of AppComponent');
  }
}
