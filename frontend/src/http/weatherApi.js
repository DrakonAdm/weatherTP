import {$host, $authHost} from "./index";

export const getWeatherMain = async () => {
    const response = await $host.get('api/today')
    return response
}

export const getWeatherTomorrow = async (date) => {
    const response = await $host.get('api/tomorrow', + date)
    return response
}

export const getWeather10Days = async () => {
    const response = await $host.get('api/weather/10days')
    return response
}

export const getWeatherMonth = async () => {
    const response = await $host.get('api/weather/month')
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


