import {makeAutoObservable} from "mobx";

export default class User {
    constructor() {
        this._isAuth = false
        this._isAdmin = false
        this._user = {}
        makeAutoObservable(this)
    }

    setIsAuth(bool) {
        this._isAuth = bool
    }

    setIsAdmin(bool) {
        this._isAdmin = bool
    }

    setUser(user) {
        this._user = user
    }

    get isAuth() {
        return this._isAuth
    }

    get isAdmin() {
        return this._isAdmin
    }

    get user() {
        return this._user
    }

}