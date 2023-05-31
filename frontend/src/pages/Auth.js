import React from 'react';
import {NavLink, useLocation} from "react-router-dom";
import {Button, Card, Container, Form} from "react-bootstrap";
import {LOGIN_ROUTE, REGISTRATION_ROUTE} from "../utils/consts";

const Auth = () => {
    return (
        <Container
            className="d-flex justify-content-center align-items-center"
            style = {{height: window.innerHeight - 100}}
        >
            <Card style={{width: 600, borderWidth: 0}} className="p-4">
                <h2 className="m-auto">Авторизация</h2>
                <h5 className="mt-4 me-left">Введите Email:</h5>
                <Form.Control
                    className="mt-3"
                    placeholder="email"
                />
                <h5 className="mt-4 me-left">Введите пароль:</h5>
                <Form.Control
                    className="mt-3"
                    placeholder="password"
                />
                <Button
                    variant={"outline-success"}
                    className="mt-3 align-self-center"
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