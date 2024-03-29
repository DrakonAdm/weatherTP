import React, {useContext} from 'react';
import {Routes, Roure, Navigate, Route} from 'react-router-dom'
import {authRoutes, publicRoutes, adminRoutes} from "../routes";
import {HOME_ROUTE} from "../utils/consts";
import {Context} from "../context";

const AppRouter = () => {
    const {user} = useContext(Context)
    return (
        <Routes>
            {/*{user.isAdmin && adminRoutes.map(({path, Component}) =>
                <Route key={path} path={path} element={<Component/>} exact/>
            )}*/}
            {user.isAuth && authRoutes.map(({path, Component}) =>
                <Route key={path} path={path} element={<Component/>} exact/>
            )}
            {publicRoutes.map(({path, Component}) =>
                <Route key={path} path={path} element={<Component/>} exact/>
            )}
            <Route path='*' element={<Navigate to={HOME_ROUTE}/>} />
        </Routes>
    );
};

export default AppRouter;