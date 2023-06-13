import {$host, $authHost} from "./index";

export const getWeatherMain = async (city) => {
    const {response} = await $host.get('/date', {
        city: city
    })
    return response
}

export const getWeatherDate = async (date, city) => {
    const {response} = await $host.get('/date', {
        date: date,
        city: city
    })
    return response
}


export const getClothes = async () => {
    const {response} = await $host.get('/clothes')
    return response
}

export const getWeatherTomorrow = async (tomorrow, city) => {
    const {response} = await $host.get('/date', {
        tomorrow: tomorrow,
        city: city
    })
    return response
}

export const getWeather5Days = async (days, city) => {
    const {response} = await $host.get('/days', {
        days: days,
        city: city
    })
    return response
}

/*export const getWeatherMonth = async () => {
    const response = await $host.get('/days')
    return response
}*/

export const getStatistic = async (page, page_size = 5, country, city, date1, date2) => {
    const {response} = await $host.get('/statisticPast', {
        page: page,
        page_size: page_size,
        country: country,
        city: city,
        firstDate: date1,
        secondDate: date2
    }) //пагинацию добавить
    return response
}

export const getAbnormal = async (country, city, date1, date2) => {
    const {response} = await $authHost.get('/statisticAbnormal', {
        country: country,
        city: city,
        firstDate: date1,
        secondDate: date2
    })
    return response
}

export const getAd = async (short) => {
    const {response} = await $host.get('/advertisementGET', {
        short: short
    })
    return response
}


export function getDate() {
    const today = new Date();
    const year = today.getFullYear();
    const month = String(today.getMonth() + 1).padStart(2, '0');
    const date = String(today.getDate()).padStart(2, '0');

    return year + "-" + month + "-" + date;
}

export function getDate5() {
    const today = new Date();
    const year = today.getFullYear();
    const month = String(today.getMonth() + 1).padStart(2, '0');
    const date = String(today.getDate() + 5).padStart(2, '0');

    return year + "-" + month + "-" + date;
}