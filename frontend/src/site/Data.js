import {makeAutoObservable} from "mobx";
import React from "react";

export default class Data {
    constructor() {

        this._weatherDay = []

        this._weather5Days = []

        this._weatherMonth = []

        this._statistic = []

        this._abnormal = []

        this._clothes = []

        this._listCities = []

        this._cityCountry = []

        this._page = []

        this._statPage = 1
        this._statTotalCount = 0
        this._statLimit = 3

        makeAutoObservable(this)
    }

    setWeatherDay(weather) {
        this._weatherDay[0] = weather
    }

    setWeather5Days(weather) {
        this._weather5Days= weather
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

    setCityCountry(cityCountry) {
        this._cityCountry = cityCountry
    }

    setPage(page) {
        this._page[0] = page;
    }


    setListCities(list) {
        this._listCities = list;
    }


    setStatPage(page) {
        this._statPage = page
    }

    setTotalCount(count) {
        this._statTotalCount = count
    }


    get weatherDay() {
        return this._weatherDay
    }

    get weather5Days() {
        return this._weather5Days
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

    get cityCountry() {
        return this._cityCountry
    }

    get page() {
        return this._page
    }


    get listCities() {
        return this._listCities
    }

    get statPage() {
        return this._statPage
    }

    get statLimit() {
        return this._statLimit
    }

    get statTotalCount() {
        return this._statTotalCount
    }

}