import { Injectable } from '@angular/core';
import { Http, Response } from '@angular/http';
import { Observable } from 'rxjs/Observable';
import 'rxjs/add/operator/map';
import 'rxjs/add/operator/catch';
import 'rxjs/add/operator/do';
import {AuthHttp} from "angular2-jwt";
import {GeneralLib} from "../lib";


@Injectable()
export class AuthService {
    private _apiUrl;

    constructor(private _http: Http, public authHttp: AuthHttp) {
      this._apiUrl = GeneralLib.serverUrl;
    }

    logIn(email, password): any {
        return this._http.post(`${this._apiUrl}/api-token-auth/`, {email, password})
            .map((response: Response) => response.json())
            .do(data => console.log(data))
            .catch(this.handleError);
    }

    getUsers(): any {
        return this.authHttp.get(`${this._apiUrl}/my_auth/api/my_user_list/`)
          .map((response: Response) => response.json())
          .do(data => console.log(data))
          .catch(this.handleError);
    }


    private handleError(error: Response) {
        console.error(error);
        return Observable.throw(error.json().error || 'Server error');
    }
}
