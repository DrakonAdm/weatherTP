import {$host, $authHost} from "./index";

export const getWeatherDay = async (country, city, date) => {
    const response = await $host.get('api/weather', + country + city + date) //тут api по которому получать
    return response
}

export const getWeather10Days = async (country, city) => {
    const response = await $host.get('api/weather/10days', + country + city)
    return response
}

export const getWeatherMonth = async (country, city) => {
    const response = await $host.get('api/weather/month', + country + city)
    return response
}

export const getStatistic = async (country, city, date1, date2) => {
    const response = await $host.get('api/weather/statistic', + country + city + date1 + date2)
    return response
}

export const getAbnormal = async (country, city, date1, date2) => {
    const response = await $host.get('api/weather/abnormal', + country + city + date1 + date2)
    return response
}


