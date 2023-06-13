import {makeAutoObservable} from "mobx";

export default class User {
    constructor() {
        this._isAuth = false
/*        this._isAdmin = false*/
        this._user = {}
        this._chooseCity = ""
        makeAutoObservable(this)
    }

    setIsAuth(bool) {
        this._isAuth = bool
    }

/*    setIsAdmin(bool) {
        this._isAdmin = bool
    }*/

    setUser(user) {
        this._user = user
    }

    setChooseCity(city) {
        this._chooseCity = city
    }

    get isAuth() {
        return this._isAuth
    }

  /*  get isAdmin() {
        return this._isAdmin
    }*/

    get user() {
        return this._user
    }

    get chooseCity() {
        return this._chooseCity;
    }

}