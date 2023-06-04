import React, {useContext, useState} from 'react';
import {NavLink, useLocation, useNavigate} from "react-router-dom";
import {Button, Card, Container, Form} from "react-bootstrap";
import {HOME_ROUTE, LOGIN_ROUTE, REGISTRATION_ROUTE} from "../utils/consts";
import {login, registration} from "../http/userApi";
import {Context} from "../index";

const Auth = () => {
    document.body.style.background = "#FFFAF4";

    const {user} = useContext(Context)
    const {history} = useNavigate();

    const [email, setEmail] = useState('')
    const [password, setPassword] = useState('')

    const click = async () => {
        let data = await login(email, password)
        user.setUser(data)
        user.setIsAuth(true)
        history.navigate(HOME_ROUTE)
    }
    return (
        <Container
            className="d-flex justify-content-center align-items-center"
            style = {{height: window.innerHeight - 100}}
        >
            <Card style={{width: 600, borderWidth: 0, backgroundColor: "#FFFAF4"}} className="p-4">
                <h2 className="m-auto">Авторизация</h2>
                <h5 className="mt-4 me-left">Введите Email:</h5>
                <Form.Control
                    className="mt-3"
                    placeholder="email"
                    value={email}
                    onChange={e => setEmail(e.target.value)}

                />
                <h5 className="mt-4 me-left">Введите пароль:</h5>
                <Form.Control
                    className="mt-3"
                    placeholder="password"
                    type="password"
                    value={password}
                    onChange={e => setPassword(e.target.value)}
                />
                <Button
                    variant={"outline-dark"}
                    className="mt-3 align-self-center"
                    onClick={click}
                >
                    Войти
                </Button>
                    <div className="mt-5 text-center" >
                        Еще не зарегистрированы? <NavLink to={REGISTRATION_ROUTE} variant={"outline-success"}>Регистрация </NavLink>
                    </div>
                </Card>
        </Container>
    );
};

export default Auth;