import React from 'react';
import {Button, Card, Container, Form} from "react-bootstrap";
import {NavLink} from "react-router-dom";
import {LOGIN_ROUTE} from "../utils/consts";

const Registration = () => {
    document.body.style.background = "#FFFAF4";
    return (
        <Container
            className="d-flex justify-content-center align-items-center"
            style={{height: window.innerHeight - 100}}
        >
            <Card style={{width: 600, borderWidth: 0, backgroundColor: "#FFFAF4"}} className="p-4">
                <h2 className="m-auto">Регистрация</h2>
                <h5 className="mt-4 me-left">Введите имя:</h5>
                <Form.Control
                    className="mt-3"
                    placeholder="name"
                />
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
                <h5 className="mt-4 me-left">Повторите пароль:</h5>
                <Form.Control
                    className="mt-3"
                    placeholder="password"
                />
                <Button
                    variant={"outline-success"}
                    className="mt-3 align-self-center"
                >
                    Зарегистрироваться
                </Button>
                <div className="mt-5 text-center">
                    Уже зарегистрированы? <NavLink to={LOGIN_ROUTE} variant={"outline-success"}>Войти </NavLink>
                </div>
            </Card>
        </Container>
    );
};

export default Registration;