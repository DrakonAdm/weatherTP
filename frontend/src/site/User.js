import {makeAutoObservable} from "mobx";

export default class User {
    constructor() {
        window.addEventListener('beforeunload', () => {
            // Удаляем ключи из localStorage, связанные с данными пользователя
            localStorage.removeItem('userData');
            localStorage.removeItem('isAuth');
            localStorage.removeItem('chooseCity');
        });

        this._isAuth = false;
        this._user = {};
        this._chooseCity = localStorage.getItem('chooseCity') || '';

        this.loadUserState();

        makeAutoObservable(this);
    }

    loadUserState() {
        const userData = localStorage.getItem('userData');
        const isAuth = localStorage.getItem('isAuth');

        try {

            if (userData === undefined) {
                this.setIsAuth(false)
            }

            if (userData !== undefined) {
                this._user = JSON.parse(userData);
            }
        } catch (error) {
            console.error('Error parsing userData:', error);
        }

        if (isAuth !== undefined && isAuth !== null) {
            this._isAuth = JSON.parse(isAuth);
        }
    }

    saveUserState() {
        localStorage.setItem('userData', JSON.stringify(this._user));
        localStorage.setItem('isAuth', JSON.stringify(this._isAuth));
    }

    // Setters

    setIsAuth(bool) {
        this._isAuth = bool;
        this.saveUserState();
    }

    setUser(user) {
        this._user = user;
        this.saveUserState();
    }

    setChooseCity(city) {
        this._chooseCity = city;
        localStorage.setItem('chooseCity', city);
    }
    // Getters

    get isAuth() {
        return this._isAuth;
    }

    get user() {
        return this._user;
    }

    get chooseCity() {
        return this._chooseCity;
    }
}