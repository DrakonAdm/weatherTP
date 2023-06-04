import {makeAutoObservable} from "mobx";

export default class Weather {
    constructor() {
        this._weather = [
            {id: 1, date:'23/03/23', minTemp: 12, maxTemp: 20, avgTemp: 16, pressure: 740, windSpeed: 3, rainfall: 0, idCity: 1},
            {id: 1, date:'24/03/23', minTemp: 12, maxTemp: 20, avgTemp: 16, pressure: 740, windSpeed: 3, rainfall: 0, idCity: 1},
            {id: 1, date:'25/03/23', minTemp: 12, maxTemp: 20, avgTemp: 16, pressure: 740, windSpeed: 3, rainfall: 0, idCity: 1},
            {id: 1, date:'26/03/23', minTemp: 12, maxTemp: 20, avgTemp: 16, pressure: 740, windSpeed: 3, rainfall: 0, idCity: 1},
            {id: 1, date:'27/03/23', minTemp: 12, maxTemp: 23, avgTemp: 16, pressure: 740, windSpeed: 3, rainfall: 0, idCity: 1},
            {id: 1, date:'28/03/23', minTemp: 12, maxTemp: 20, avgTemp: 16, pressure: 740, windSpeed: 3, rainfall: 0, idCity: 1},
            {id: 1, date:'29/03/23', minTemp: 12, maxTemp: 20, avgTemp: 16, pressure: 740, windSpeed: 3, rainfall: 0, idCity: 1},
            {id: 1, date:'30/03/23', minTemp: 12, maxTemp: 20, avgTemp: 16, pressure: 740, windSpeed: 3, rainfall: 0, idCity: 1},
            {id: 1, date:'23/03/23', minTemp: 12, maxTemp: 20, avgTemp: 26, pressure: 740, windSpeed: 3, rainfall: 0, idCity: 1},
            {id: 1, date:'23/03/23', minTemp: 12, maxTemp: 20, avgTemp: 16, pressure: 740, windSpeed: 3, rainfall: 0, idCity: 1},
            {id: 1, date:'23/03/23', minTemp: 12, maxTemp: 20, avgTemp: 16, pressure: 740, windSpeed: 3, rainfall: 0, idCity: 1},
            {id: 1, date:'24/03/23', minTemp: 12, maxTemp: 20, avgTemp: 16, pressure: 740, windSpeed: 3, rainfall: 0, idCity: 1},
            {id: 1, date:'25/03/23', minTemp: 12, maxTemp: 20, avgTemp: 16, pressure: 740, windSpeed: 3, rainfall: 0, idCity: 1},
            {id: 1, date:'26/03/23', minTemp: 12, maxTemp: 20, avgTemp: 16, pressure: 740, windSpeed: 3, rainfall: 0, idCity: 1},
            {id: 1, date:'27/03/23', minTemp: 12, maxTemp: 23, avgTemp: 16, pressure: 740, windSpeed: 3, rainfall: 0, idCity: 1},
            {id: 1, date:'28/03/23', minTemp: 12, maxTemp: 20, avgTemp: 16, pressure: 740, windSpeed: 3, rainfall: 0, idCity: 1},
            {id: 1, date:'29/03/23', minTemp: 12, maxTemp: 20, avgTemp: 16, pressure: 740, windSpeed: 3, rainfall: 0, idCity: 1},
            {id: 1, date:'30/03/23', minTemp: 12, maxTemp: 20, avgTemp: 16, pressure: 740, windSpeed: 3, rainfall: 0, idCity: 1},
            {id: 1, date:'23/03/23', minTemp: 12, maxTemp: 20, avgTemp: 26, pressure: 740, windSpeed: 3, rainfall: 0, idCity: 1},
            {id: 1, date:'23/03/23', minTemp: 12, maxTemp: 20, avgTemp: 16, pressure: 740, windSpeed: 3, rainfall: 0, idCity: 1},
        ]
        this._statistic = [
            {id: 1, date:'23/03/23', minTemp: 12, maxTemp: 20, avgTemp: 16, pressure: 740, windSpeed: 3, rainfall: 0, idCity: 1},
            {id: 1, date:'23/03/23', minTemp: 12, maxTemp: 20, avgTemp: 16, pressure: 740, windSpeed: 3, rainfall: 0, idCity: 1},
            {id: 1, date:'23/03/23', minTemp: 12, maxTemp: 20, avgTemp: 16, pressure: 740, windSpeed: 3, rainfall: 0, idCity: 1},
            {id: 1, date:'23/03/23', minTemp: 12, maxTemp: 20, avgTemp: 16, pressure: 740, windSpeed: 3, rainfall: 0, idCity: 1},
            {id: 1, date:'23/03/23', minTemp: 12, maxTemp: 20, avgTemp: 16, pressure: 740, windSpeed: 3, rainfall: 0, idCity: 1},
            {id: 1, date:'23/03/23', minTemp: 12, maxTemp: 20, avgTemp: 16, pressure: 740, windSpeed: 3, rainfall: 0, idCity: 1},
            {id: 1, date:'23/03/23', minTemp: 12, maxTemp: 20, avgTemp: 16, pressure: 740, windSpeed: 3, rainfall: 0, idCity: 1},
        ]
        this._abnormal = [
            {id: 1, idTown: 1, minTemp: 12, maxTemp: 20, maxRainfall: 16, maxWindSpeed: 34}, //Здесь нужно брать id дня аномалий
            {id: 1, idTown: 1, minTemp: 12, maxTemp: 20, maxRainfall: 16, maxWindSpeed: 34},
            {id: 1, idTown: 1, minTemp: 12, maxTemp: 20, maxRainfall: 16, maxWindSpeed: 34},
            {id: 1, idTown: 1, minTemp: 12, maxTemp: 20, maxRainfall: 16, maxWindSpeed: 34},
        ]

        this._clothes = [
            "Куртка, футболка, джинсы, кроссовки"
        ]

        this._city = [
            {id: 1, town: "Город", country: "Страна1"},
            {id: 1, town: "Город1", country: "Страна1"},
            {id: 1, town: "Город2", country: "Страна1"},
            {id: 1, town: "Город3", country: "Страна1"},
            {id: 1, town: "Город4", country: "Страна2"},
            {id: 1, town: "Город5", country: "Страна2"},
        ]
        makeAutoObservable(this)
    }

    setWeather(weather) {
        this._weather= weather
    }

    setStatistics(statistic) {
        this._statistic = statistic
    }

    setAbnormal(abnormal) {
        this._abnormal = abnormal
    }

    setClothes(clothes) {
        this._clothes = clothes
    }

    get weather() {
        return this._weather
    }

    get statistics() {
        return this._statistic
    }

    get abnormal() {
        return this._abnormal
    }

    get clothes() {
        return this._clothes
    }

}