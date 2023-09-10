import {$host, $authHost} from "./index";

export const getWeatherMain = async (city) => {
   return await $host.get(`/today/?city=${city}`);
}

export const getWeatherDate = async (date, city) => {
    return await $host.get(`/date?date=${date}&city=${city}`);
}

export const getWeatherTomorrow = async (tomorrow, city) => {
    return await $host.get(`/tomorrow?city=${city}&tomorrow=${tomorrow}`);
}

export const getClothes = async () => {
    const {response} = await $host.get('/clothes')
    return response
}

export const getWeather5Days = async (city) => {
    return await $host.get(`/days?city=${city}`);
}

/*export const getWeatherMonth = async () => {
    const response = await $host.get('/days')
    return response
}*/

export const getStatistic = async (page, page_size = 10, country, city, date1, date2) => {
    return await $host.get(`/statisticPast/?page=${page}&page_size=${page_size}&country=${country}&city=${city}&firstDate=${date1}&secondDate=${date2}`)
}

export const getAbnormal = async (page, page_size = 10, country, city, date1, date2) => {
    return await $authHost.get(`/statisticAbnormal/?page=${page}&page_size=${page_size}&country=${country}&city=${city}&firstYear=${date1}&secondYear=${date2}`)
}

export const getAd = async (short) => {
    const {response} = await $host.get(`/advertisementGET/?short=${short}`)
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

export const getListCity = async () => {
    const response = await $host.get(`/listCity/`);
    return response.data.cities;
}

export const getListCityCountry = async () => {
    const response = await $host.get(`/listCC/`);
    return response.data;
}
