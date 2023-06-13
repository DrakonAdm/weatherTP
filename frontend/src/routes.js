import {
    HOME_ROUTE,
    TOMORROW_ROUTE,
    DAYS_ROUTE,
    DATE_ROUTE,
    STATISTIC_ROUTE,
    ARCHIVE_ROUTE,
    ABNORMAL_ROUTE,
    LOGIN_ROUTE,
    REGISTRATION_ROUTE,
    PROFILE_USER_ROUTE,
} from "./utils/consts";
import Home from "./pages/Home";
import Tomorrow from "./pages/Tomorrow";
import Days from "./pages/Days";
import Date from "./pages/Date";
import Statistic from "./pages/Statistic";
import Archive from "./pages/Archive";
import Auth from "./pages/Auth";
import Abnormal from "./pages/Abnormal";
import ProfileUser from "./pages/ProfileUser";
import Registration from "./pages/Registration";


export const publicRoutes = [
    {
        path: HOME_ROUTE,
        Component: Home
    },
    {
        path: TOMORROW_ROUTE,
        Component: Tomorrow
    },
    {
        path: DAYS_ROUTE,
        Component: Days
    },
   /* {
        path: MONTH_ROUTE,
        Component: Month
    },*/
    {
        path: DATE_ROUTE,
        Component: Date
    },
    {
        path: STATISTIC_ROUTE,
        Component: Statistic
    },
    {
        path: ARCHIVE_ROUTE,
        Component: Archive
    },
    {
        path: LOGIN_ROUTE,
        Component: Auth
    },
    {
        path: REGISTRATION_ROUTE,
        Component: Registration
    },

]

export const authRoutes = [

    {
        path: ABNORMAL_ROUTE,
        Component: Abnormal
    },
    {
        path: PROFILE_USER_ROUTE,
        Component: ProfileUser
    },

]

/*
export const adminRoutes = [
    {
        path: PROFILE_ADMIN_ROUTE,
        Component: ProfileAdmin
    },
    {
        path: CHANGE_AD_ROUTE,
        Component: ChangeAd
    },
    {
        path: USERS_ROUTE,
        Component: Users
    },

]*/
