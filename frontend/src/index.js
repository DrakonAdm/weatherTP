import React, {createContext} from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
import User from "./site/User";
import Weather from "./site/Weather";
import Users from "./site/Users";

export const Context = createContext(null)

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
    <Context.Provider value = {{
        user: new User(),
        weather: new Weather(),
        users: new Users(),
    }}>
        <App />
    </Context.Provider>,
);
