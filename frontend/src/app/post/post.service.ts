import { Injectable } from '@angular/core';

import {Http, Response} from "@angular/http";
import {AuthHttp} from "angular2-jwt";

import {GeneralLib} from "../lib";
import {Observable} from "rxjs";

@Injectable()
export class PostService {

  private _apiUrl;

  constructor(private _http: Http, private _authHttp: AuthHttp) {
    this._apiUrl = GeneralLib.serverUrl;
  }

  getPosts(url): any {
    return this._authHttp.get(url)
      .map((response: Response) => response.json() )
      .do(data => console.log(data) )
      .catch(this.handleError);
  }
  makeSympathy(id: number, sympathy: Boolean): any {
    let symp = (sympathy)? "like": "dislike";
    return this._authHttp.post(`${this._apiUrl}/post/posts/${id}/${symp}/`, {})
      .map((response: Response) => response.json() )
      .do(data => console.log(data) )
      .catch(this.handleError);
  }

  private handleError(error: Response) {
      console.error(error);
      return Observable.throw(error.json().error || 'Server error');
    }
}
