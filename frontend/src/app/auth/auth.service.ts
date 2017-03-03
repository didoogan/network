import { Injectable } from '@angular/core';
import { Http, Response } from '@angular/http';
import { Observable } from 'rxjs/Observable';
import 'rxjs/add/operator/map';
import 'rxjs/add/operator/catch';
import 'rxjs/add/operator/do';


@Injectable()
export class AuthService {
    private _apiUrl = 'http://127.0.0.1:8000';

    constructor(private _http: Http) {}

    logIn(email, password): any {
        return this._http.post(`${this._apiUrl}/api-token-auth/`, {email, password})
            .map((response: Response) => response.json())
            .do(data => console.log(data))
            .catch(this.handleError);
    }


    private handleError(error: Response) {
        console.error(error);
        return Observable.throw(error.json().error || 'Server error');
    }
}
