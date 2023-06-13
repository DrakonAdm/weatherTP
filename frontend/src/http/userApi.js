import {$host, $authHost} from "./index";

export const registration = async (email, password, nickname, city, country) => {
    const response = await $host.post('/register', {email, password, nickname, city, country})
    return response
}

export const login = async (email, password) => {
    const response = await $host.post('/login', {email, password})
    return response
}

export const logout = async () => {
    const response = await $host.post('/logout',)
    return response
}

export const check = async () => {
    const response = await $host.post('/register')
    return response
}

export const getInfo = async (name) => {
    const response = await $host.get('api/user', name)
    return response
}

export const setCityCountry = async (city, country) => {
    const response = await $host.post('/setCity', {city, country})
    return response
}

export const setNewPassword = async (newPassword) => {
    const response = await $host.post('/setPassword', {newPassword})
    return response
}
