import {makeAutoObservable} from "mobx";

export default class Users {
    constructor() {
        this._listUsers = [
            {id: 1, name: "Имя", email: "Почта"},
            {id: 1, name: "Имя", email: "Почта"},
            {id: 1, name: "Имя", email: "Почта"},
            {id: 1, name: "Имя", email: "Почта"},
            {id: 1, name: "Имя", email: "Почта"},
            {id: 1, name: "Имя", email: "Почта"},
        ]
        makeAutoObservable(this)
    }

    setUsers(users) {
        this._listUsers = users
    }

    get listUsers() {
        return this._listUsers
    }

}