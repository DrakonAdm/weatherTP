import React from 'react';
import {Button, Card, CardGroup, Col, Container, Form, Row} from "react-bootstrap";
import {NavLink} from "react-router-dom";
import {ABNORMAL_ROUTE, ARCHIVE_ROUTE, REGISTRATION_ROUTE} from "../utils/consts";
import '../components/App.css'

const Statistic = () => {
    document.body.style.background = "#FFFAF4";
    return (
        <Container style={{height: window.innerHeight - 50, width: window.innerWidth - 500, backgroundColor: "#FFFAF4"}}>
            <CardGroup>
                <Card style={{width: 900, backgroundColor: "#FFFAF4", borderWidth: 0}} className="p-5">
                    <Button
                        variant={"outline-dark"}
                        className="button_menu"
                        href={ARCHIVE_ROUTE}
                    >
                        Статистика за прошедшие годы
                    </Button>
                </Card>
                <Card style={{width: 900, backgroundColor: "#FFFAF4", borderWidth: 0}} className="p-5">
                    <Button
                        variant={"outline-dark"}
                        className="button_menu"
                        href={ABNORMAL_ROUTE}
                    >
                        Статистика аномальной погоды
                    </Button>
                </Card>
            </CardGroup>
            <Row>
                <Col sm={6}>
                <Card style={{width: 450, backgroundColor: "#FFFAF4", borderWidth: 0}} className="p-4">
                        <div>
                        В этом разделе вы можете увидеть статистику погоды по дням
                        по показателям: <br />
                        1. Минимальная температура
                        <br />
                        2. Максимальная температура
                        <br />
                        3. Средняя температура
                        <br />
                        4. Атмосферное давление
                        <br />
                        5. Скорость ветра
                        <br />
                        6. Осадки
                        <br />
                        Вам нужно будет выбрать страну, город и даты начала и
                        окончания запрашиваемой статистики.
                    </div>
                </Card>
                </Col>
                <Col sm={6}>
                <Card style={{width: 450, backgroundColor: "#FFFAF4", borderWidth: 0}} className="p-4">
                    <div>
                        В этом разделе вы можете увидеть аномальные показатели
                        погоды (когда показатели принимают значения, сильно
                        отличающиеся от среднестатистических за определенный период
                        времени). <br />
                        Вам нужно будет выбрать страну, город и года начала и
                        окончания периодов, в которых будет отображаться аномальная
                        погода, а именно:
                        <br />
                        1. Максимальная температура
                        <br />
                        2. Минимальная температура
                        <br />
                        3. Наибольшее количество осадков
                        <br />
                        4. Наибольшая скорость ветра
                    </div>
                </Card>
                </Col>
            </Row>
        </Container>
    );
};

export default Statistic;