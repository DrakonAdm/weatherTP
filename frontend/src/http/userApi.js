import {$host, $authHost} from "./index";

export const registration = async (email, password, country, city) => {
    const response = await $host.post('api/auth/registration', {email, password, country, city}) //тут api по которому передавать
    return response
}

export const login = async (email, password) => {
    const response = await $host.post('api/auth/login', {email, password})
    return response
}

export const check = async () => {
    const response = await $host.post('api/auth/registration') //тут api по которому передавать
    return response
}

export const getInfo = async (name) => {
    const response = await $host.get('api/user' + name) //тут api по которому получать
    return response
}
//получение инфы о пользователе для лк видимо