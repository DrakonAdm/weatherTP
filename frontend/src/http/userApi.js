import {$host, $authHost} from "./index";

export const registration = async (email, password, nickname, city, country) => {
    const response = await $host.post(`/register/?email=${email}&password=${password}&nickname=${nickname}&country=${country}&city=${city}`)
    return response
}

export const login = async (email, password) => {
    const response = await $host.post(`/login/?email=${email}&password=${password}`)
    return response
}

export const logout = async () => {
    const response = await $host.post('/logout/',)
    return response
}

export const check = async () => {
    const response = await $host.post('/register/')
    return response
}

export const setCityCountry = async (email, password, city, country) => {
    const response = await $authHost.get(`/accountUser/?email=${email}&password=${password}&country=${country}&city=${city}`)
    return response
}



// export const setNewPassword = async (email, password, newPassword) => {
//     const response = await $authHost.post(`/accountUser/?email=${email}&password=${password}&pass=${newPassword}`)
//     return response
// }
