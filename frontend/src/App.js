import React, {useContext, useEffect, useState} from 'react';
import {BrowserRouter} from "react-router-dom";
import AppRouter from "./components/AppRouter";
import NavBar from "./components/NavBar";
import {observer} from "mobx-react-lite";
import {Context} from "./context/index.js";
import {check} from "./http/userApi";
import User from "./site/User";
import Data from "./site/Data";

const App = observer(() => {
  const [user, setUser] = useState(new User());
  const [data, setData] = useState({});
  const [loading, setLoading] = useState(true)

  useEffect(() => {
      check().then( data => {
          user.setUser(true)
          user.setIsAuth(true)
      }).finally(() => setLoading(false))
  }, [])

  return (
    <Context.Provider value = {{
      user: user,
      data: data,
      setData: setData,
    }}>
      <BrowserRouter>
          <NavBar />
          <AppRouter />
      </BrowserRouter>
    </Context.Provider>
  );
});

export default App;
