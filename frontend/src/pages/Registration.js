import React, {useContext, useState} from 'react';
import {Alert, Button, Card, Col, Container, Form, Row} from "react-bootstrap";
import {NavLink, useNavigate} from "react-router-dom";
import {HOME_ROUTE, LOGIN_ROUTE} from "../utils/consts";
import {login, registration} from "../http/userApi";
import {observer} from "mobx-react-lite";
import {Context} from "../context";

const Registration = observer (() => {
    document.body.style.background = "#FFFAF4";

    const {user} = useContext(Context)
    const navigate = useNavigate();

    const [name, setName] = useState('')
    const [email, setEmail] = useState('')
    const [password, setPassword] = useState('')
    const [repPassword, setRepPassword] = useState('')
    const [country, setCountry] = useState('')
    const [city, setCity] = useState('')
    /*const [pasError, setPasError] = useState('');*/
    const [passwordsMatch, setPasswordsMatch] = useState(true);

    const click = async () => {
        try {
            let data = await registration(email, password, name, city, country)
            user.setUser(data.data)
            user.setChooseCity(data.data.city)
            user.setIsAuth(true)
            navigate(HOME_ROUTE)
        } catch (e) {
            alert(e.response.data.message)
        }
    }

    const isFormValid = () => {
        return email !== '' && name !== '' && password !== '' && repPassword !== '' ;
    }

    const handlePasswordChange = (event) => {
        setPassword(event.target.value);
        setPasswordsMatch(event.target.value === repPassword);
    };

    const handlePasswordRepeatChange = (event) => {
        setRepPassword(event.target.value);
        setPasswordsMatch(event.target.value === password);
    };

    return (
        <div className="background">
        <Container
            className="d-flex justify-content-center align-items-center"
            style={{height: window.innerHeight - 50}}
        >
            <Card style={{width: 600, borderWidth: 0, backgroundColor: "transparent"}} className="p-4">
                <h2 className="m-auto">Регистрация</h2>
                <Form>
                <h5 className="mt-4 me-left">Введите имя*:</h5>
                <Form.Control
                    className="mt-3"
                    placeholder="name"
                    value={name}
                    onChange={e => setName(e.target.value)}
                />
                <h5 className="mt-4 me-left">Введите Email*:</h5>
                <Form.Control
                    className="mt-3"
                    placeholder="email"
                    type="email"
                    value={email}
                    onChange={e => setEmail(e.target.value)}
                />
                <Row className="d-flex">
                    <Col>
                        <h5 className="mt-4 me-left">Введите пароль*:</h5>
                        <Form.Control
                            className="mt-3"
                            placeholder="пароль"
                            type="password"
                            value={password}
                            onChange={handlePasswordChange}
                        />
                    </Col>
                    <Col>
                        <h5 className="mt-4 me-left">Повторите пароль*:</h5>
                        <Form.Control
                            className="mt-3"
                            placeholder="пароль"
                            type="password"
                            value={repPassword}
                            onChange={handlePasswordRepeatChange}
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
                    {!passwordsMatch && <div style={{ color: 'red', left: 0}} className="mt-3 text-center">Пароли не совпадают</div>}
                    {!isFormValid() && <div style={{ color: 'red',  }} className="mt-3 text-center">Заполните обязательные поля (отмечены *)</div>}
                </Form>
                <Button
                    variant={"outline-dark"}
                    className="mt-3 align-self-center"
                    onClick={click}
                    type="submit"
                    disabled={!passwordsMatch || !isFormValid()}
                >
                    Зарегистрироваться
                </Button>
                <div className="mt-5 text-center">
                    Уже зарегистрированы? <NavLink to={LOGIN_ROUTE} variant={"outline-success"}>Войти </NavLink>
                </div>
            </Card>
        </Container>
        </div>
    );
});

export default Registration;