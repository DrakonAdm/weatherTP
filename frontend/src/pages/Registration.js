import React, {useContext, useState} from 'react';
import {Button, Card, Col, Container, Form, Row} from "react-bootstrap";
import {NavLink} from "react-router-dom";
import {LOGIN_ROUTE} from "../utils/consts";
import {registration} from "../http/userApi";
import {observer} from "mobx-react-lite";
import {Context} from "../index";

const Registration = observer (() => {
    document.body.style.background = "#FFFAF4";

    const {user} = useContext(Context)

    const [name, setName] = useState('')
    const [email, setEmail] = useState('')
    const [password, setPassword] = useState('')
    const [repPassword, setRepPassword] = useState('')
    const [country, setCountry] = useState('')
    const [city, setCity] = useState('')

    const click = async () => {
        let data = await registration(email, password, country,  city)
        user.setUser(data)
        user.setIsAuth(true)
    }

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
                    value={name}
                    onChange={e => setName(e.target.value)}
                />
                <h5 className="mt-4 me-left">Введите Email:</h5>
                <Form.Control
                    className="mt-3"
                    placeholder="email"
                    value={email}
                    onChange={e => setEmail(e.target.value)}
                />
                <Row className="d-flex">
                    <Col>
                        <h5 className="mt-4 me-left">Введите пароль:</h5>
                        <Form.Control
                            className="mt-3"
                            placeholder="пароль"
                            type="password"
                            value={password}
                            onChange={e => setPassword(e.target.value)}
                        />
                    </Col>
                    <Col>
                        <h5 className="mt-4 me-left">Повторите пароль:</h5>
                        <Form.Control
                            className="mt-3"
                            placeholder="пароль"
                            type="password"
                            value={repPassword}
                            onChange={e => setRepPassword(e.target.value)}
                        />
                    </Col>
                </Row>
                <p></p>
                <Row>
                    <Col>
                        <h7 className="mt-4 me-left">Введите страну:</h7>
                        <Form.Control
                            className="mt-3"
                            placeholder="Страна"
                            value={country}
                            onChange={e => setCountry(e.target.value)}
                        />
                    </Col>
                    <Col>
                        <h7 className="mt-4 me-left">Введите город:</h7>
                        <Form.Control
                            className="mt-3"
                            placeholder="Город"
                            value={city}
                            onChange={e => setCity(e.target.value)}
                        />
                    </Col>
                </Row>
                <Button
                    variant={"outline-dark"}
                    className="mt-3 align-self-center"
                    onClick={click}
                >
                    Зарегистрироваться
                </Button>
                <div className="mt-5 text-center">
                    Уже зарегистрированы? <NavLink to={LOGIN_ROUTE} variant={"outline-success"}>Войти </NavLink>
                </div>
            </Card>
        </Container>
    );
});

export default Registration;