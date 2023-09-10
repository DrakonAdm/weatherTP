import React, {useContext, useState} from 'react';
import {observer} from "mobx-react-lite";
import {Context} from "../context";
import {Button, Card, Col, Container, Form, Row} from "react-bootstrap";
import {HOME_ROUTE, PROFILE_USER_ROUTE} from "../utils/consts";
import {useNavigate} from "react-router-dom";
import {login, logout, setCityCountry, setNewPassword} from "../http/userApi";
import {getAbnormal} from "../http/weatherApi";

const ProfileUser = observer(() => {
    document.body.style.background = "#FFFAF4";
    const {user} = useContext(Context)
    const navigate = useNavigate();

    const [password, setPassword] = useState('')
    const [repPassword, setRepPassword] = useState('')
    const [passwordsMatch, setPasswordsMatch] = useState(true);

    const [country, setCountry] = useState('')
    const [city, setCity] = useState('')

    const logOut = async () => {
        try {
            user.setUser({})
            user.setIsAuth(false)
            let data = await logout();
        } catch (e) {
            alert(e.response.data.message)
        }
    }

    const changeCity = async () => {
        try {
            let data = await setCityCountry(user.user.email, user.user.password, city, country)
            console.log(data);
            user.setUser(data.data)
            user.setChooseCity(data.data.city)
            navigate(PROFILE_USER_ROUTE);
        } catch (e) {
            alert(e.response.data.message)
        }
    }

    // const changePassword = () => {
    //     try {
    //         let response = setNewPassword(password)
    //         if (response.status === 200) {
    //             // Successful response
    //             const data = response.data;
    //             console.log(data);
    //             user.setUser(data);
    //             user.setChooseCity(data.city);
    //         } else {
    //             // Handle HTTP error
    //             console.error(`HTTP Error: ${response.status} - ${response.data.message}`);
    //             // You can handle the error as needed, e.g., show a message to the user
    //         }
    //     } catch (e) {
    //         alert(e.response.data.message)
    //     }
    // }

    const handlePasswordChange = (event) => {
        setPassword(event.target.value);
        setPasswordsMatch(event.target.value === repPassword);
    };

    const handlePasswordRepeatChange = (event) => {
        setRepPassword(event.target.value);
        setPasswordsMatch(event.target.value === password);
    };

    console.log(user);

    return (
        <div className="background">
            <Container>
                <Row>
                    <Col md={4}>
                        <Card style={{width: 500, backgroundColor: "transparent", borderWidth: 0}} className="p-4">
                            <h3>Личный кабинет</h3>
                            <h4>{user.user.nickname}</h4>
                            <h4>{user.user.email}</h4>
                            <h4>
                                {user.user.country === undefined
                                    ? "Нет страны"
                                    : `${user.user.country}`}
                            </h4>
                            <h4>
                                {user.user.city === undefined
                                    ? "Нет города"
                                    : `${user.user.city}`}
                            </h4>
                        </Card>
                        <Button
                            variant={"outline-dark"}
                            className="button_menu"
                            href={HOME_ROUTE}
                            style={{
                                width: 100,
                                bottom: 200,
                                left: 100,
                            }}
                            onClick={() => logOut()}
                        >
                            Выйти
                        </Button>
                        <p></p>
                    </Col>
                    <Col>
                        <Card className="p-3 mt-4" style={{width: 400, borderWidth: 0, backgroundColor: "transparent"}}>
                            <h6 className="m-auto">Хотите изменить локацию?</h6>
                            <h7 className="mt-4 me-left">Введите страну:</h7>
                            <Form.Control
                                className="mt-3"
                                type="text"
                                placeholder="city"
                                value={country}
                                onChange={e => setCountry(e.target.value)}
                                title="Please enter only letters"
                            />
                            <h7 className="mt-4 me-left">Введите город:</h7>
                            <Form.Control
                                className="mt-3"
                                placeholder="country"
                                value={city}
                                onChange={e => setCity(e.target.value)}
                            />
                            <Button
                                variant={"outline-dark"}
                                className="mt-3 align-self-center button_menu align-items-center"
                                onClick={() => changeCity()}
                            >
                                Изменить локацию
                            </Button>
                        </Card>
                    </Col>
                    {/*<Col>*/}
                    {/*    <Card className="p-3 mt-4" style={{width: 400, borderWidth: 0, backgroundColor: "transparent"}}>*/}
                    {/*        <h6 className="m-auto">Хотите изменить пароль?</h6>*/}
                    {/*        <h7 className="mt-4 me-left">Введите старый пароль:</h7>*/}
                    {/*        <Form.Control*/}
                    {/*            className="mt-3"*/}
                    {/*            placeholder="пароль"*/}
                    {/*        />*/}
                    {/*        <h7 className="mt-4 me-left">Введите новый пароль:</h7>*/}
                    {/*        <Form.Control*/}
                    {/*            className="mt-3"*/}
                    {/*            placeholder="пароль"*/}
                    {/*            type="password"*/}
                    {/*            value={password}*/}
                    {/*            onChange={handlePasswordChange}*/}
                    {/*        />*/}
                    {/*        <h7 className="mt-4 me-left">Повторите пароль:</h7>*/}
                    {/*        <Form.Control*/}
                    {/*            className="mt-3"*/}
                    {/*            placeholder="пароль"*/}
                    {/*            type="password"*/}
                    {/*            value={repPassword}*/}
                    {/*            onChange={handlePasswordRepeatChange}*/}
                    {/*        />*/}
                    {/*        {!passwordsMatch &&*/}
                    {/*            <div style={{color: 'red', left: 0}} className="mt-3 text-center">Пароли не*/}
                    {/*                совпадают</div>}*/}
                    {/*        <Button*/}
                    {/*            variant={"outline-dark"}*/}
                    {/*            className="mt-3 align-self-center button_menu align-items-center"*/}
                    {/*            onClick={() => changePassword()}*/}
                    {/*            disabled={!passwordsMatch}*/}
                    {/*        >*/}
                    {/*            Изменить пароль*/}
                    {/*        </Button>*/}

                    {/*    </Card>*/}
                    {/*</Col>*/}
                </Row>
            </Container>
        </div>
    );
});

export default ProfileUser;