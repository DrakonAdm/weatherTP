import React, {useContext} from 'react';
import {observer} from "mobx-react-lite";
import {Context} from "../index";
import {Button, Card, Col, Container, Form, Row} from "react-bootstrap";
import {CHANGE_AD_ROUTE, HOME_ROUTE, USERS_ROUTE} from "../utils/consts";

const ProfileUser = observer(() => {
    document.body.style.background = "#FFFAF4";
    const {user} = useContext(Context)
    return (
        <Container>
            <Row>
                <Col md={4}>
                    <Card style={{width: 500, backgroundColor: "#FFFAF4", borderWidth: 0}} className="p-4">
                        <h3>Личный кабинет</h3>
                        <h4>/имя/</h4>
                        <h4>/почта/</h4>
                        <h4>/локация/</h4>
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
                    >
                        Выйти
                    </Button> {/*тут как то прописать логику выхода из лк*/}
                    <p></p>
                    <Button
                        variant={"outline-dark"}
                        className="button_menu p-2"
                        href={HOME_ROUTE}
                        style={{
                            width: 100, height: 30, fontSize: 11,
                            bottom: 70,
                            left: 100,
                        }}
                    >
                        Удалить аккаунт
                    </Button> {/*тут как то прописать логику выхода из лк*/}
                </Col>
                <Col>
                    <Card className="p-3" style={{width: 400, borderWidth: 0, backgroundColor: "#FFFAF4"}}>
                        <h6 className="m-auto">Хотите изменить локацию?</h6>
                        <h7 className="mt-4 me-left">Введите страну:</h7>
                        <Form.Control
                            className="mt-3"
                            placeholder="email"
                        />
                        <h7 className="mt-4 me-left">Введите город:</h7>
                        <Form.Control
                            className="mt-3"
                            placeholder="password"
                        />
                        <Button
                            variant={"outline-dark"}
                            className="mt-3 align-self-center button_menu align-items-center"
                        >
                            Изменить локацию
                        </Button>
                    </Card>
                    </Col>
                <Col>
                    <Card className="p-3" style={{width: 400, borderWidth: 0, backgroundColor: "#FFFAF4"}}>
                            <h6 className="m-auto">Хотите изменить пароль?</h6>
                            <h7 className="mt-4 me-left">Введите старый пароль:</h7>
                            <Form.Control
                                className="mt-3"
                                placeholder="name"
                            />
                            <h7 className="mt-4 me-left">Введите новый пароль:</h7>
                            <Form.Control
                                className="mt-3"
                                placeholder="password"
                            />
                            <h7 className="mt-4 me-left">Повторите пароль:</h7>
                            <Form.Control
                                className="mt-3"
                                placeholder="password"
                            />
                            <Button
                                variant={"outline-dark"}
                                className="mt-3 align-self-center button_menu align-items-center"
                            >
                                Изменить пароль
                            </Button>
                    </Card>
                </Col>
            </Row>
        </Container>
    );
});

export default ProfileUser;