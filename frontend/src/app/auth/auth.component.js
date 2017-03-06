"use strict";
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var core_1 = require('@angular/core');
var AuthComponent = (function () {
    function AuthComponent(_authService) {
        this._authService = _authService;
        this.title = "Lodin";
        this.email = "";
        this.password = "";
    }
    AuthComponent.prototype.logIn = function () {
        this._authService.logIn(this.email, this.password).subscribe(function (response) { return console.log(response); }, function (error) { return console.log(error); });
    };
    AuthComponent.prototype.ngOnInit = function () {
        console.log('in ngOnInit of Auth');
    };
    AuthComponent = __decorate([
        core_1.Component({
            selector: 'app-auth',
            templateUrl: './auth.component.html',
            styleUrls: ['./auth.component.css']
        })
    ], AuthComponent);
    return AuthComponent;
}());
exports.AuthComponent = AuthComponent;
