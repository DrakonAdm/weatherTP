import React, {createContext} from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
import User from "./site/User";
import Data from "./site/Data";

export const Context = createContext(null)

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
    <Context.Provider value = {{
        user: new User(),
        data: new Data(),
    }}>
        <App />
    </Context.Provider>,
);
