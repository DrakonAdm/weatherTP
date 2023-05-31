import React from 'react';
import {Button, Card, Col, Container, Form, Row} from "react-bootstrap";
import {NavLink} from "react-router-dom";
import {ABNORMAL_ROUTE, ARCHIVE_ROUTE, REGISTRATION_ROUTE} from "../utils/consts";
import '../components/App.css'

const Statistic = () => {
    return (
        <Container className='list-group-horizontal'>
            <Row>
                <Col sm={6}>
                <Card style={{width: 600}} className="p-4">
                    <Button
                        variant={"outline-success"}
                        className="statistics"
                        href={ARCHIVE_ROUTE}
                    >
                        Статистика за прошедшие годы
                    </Button>
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
                <Card style={{width: 600}} className="p-4">
                    <Button
                        variant={"outline-success"}
                        className="statistics"
                        href={ABNORMAL_ROUTE}
                    >
                        Статистика аномальной погоды
                    </Button>
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