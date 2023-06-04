import React, {useContext, useEffect, useState} from 'react';
import {Button, ButtonGroup, Card, CardGroup, Container, Dropdown, Table, Form, Row, Col} from "react-bootstrap";
import {
    ABNORMAL_ROUTE,
    ARCHIVE_ROUTE,
} from "../utils/consts";
import {observer} from "mobx-react-lite";
import {Context} from "../index";
import {getStatistic} from "../http/weatherApi";

const Archive = observer(() => {
    document.body.style.background = "#FFFAF4";
    const {weather} = useContext(Context);

    const [date1, setDate1] = useState('')
    const [date2, setDate2] = useState('')
    const [country, setCountry] = useState('')
    const [city, setCity] = useState('')

    useEffect(() => {
        getStatistic().then(data => weather.setStatistics(data))
    }, [])

    return (
        <Container
            style={{height: window.innerHeight - 50, width: window.innerWidth - 500, backgroundColor: "#FFFAF4"}}
        >
            <CardGroup>
                <Card style={{width: 900, backgroundColor: "#FFFAF4", borderWidth: 0}} className="p-5">
                    <Button
                        variant={"outline-dark"}
                        className="button_menu_active"
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
            <Card style={{width: 900, backgroundColor: "#FFFAF4", borderWidth: 0}}
                  className="d-flex align-items-center justify-content-center">
                <Row>
                    <Col>
                        <Form.Control
                            className="mt-3"
                            placeholder="Название страны"
                            value={country}
                            onChange={e => setCountry(e.target.value)}
                        />
                    </Col>
                    <Col>
                        <Form.Control
                            className="mt-3"
                            placeholder="Название города"
                            value={city}
                            onChange={e => setCity(e.target.value)}
                        />
                    </Col>
                    <Col>
                        <Form.Control
                            value={date1}
                            onChange={e => setDate1(e.target.value)}
                            className="mt-3 button-menu"
                            type="date"
                        /></Col>
                    <Col>
                        <Form.Control
                            value={date2}
                            onChange={e => setDate2(e.target.value)}
                            className="mt-3 button-menu"
                            type="date"
                        />
                    </Col>
                    <Col>
                        <Button
                            variant={"outline-dark"}
                            className="p-2 mt-3 align-self-center"
                            style={{width: 150, height: 40, fontSize: 12,}}
                        >
                            Показать статистику
                        </Button>
                    </Col>
                </Row>
            </Card>
            <Card style={{width: 900, backgroundColor: "#FFFAF4", borderWidth: 0}} className="p-5">
                <Table bordered hover7 size="sm">
                    <thead className="text-center">
                    <tr style={{backgroundColor: "#EFF8FF"}}>
                        <th>Дата</th>
                        <th>Минимальная температура</th>
                        <th>Максимальная температура</th>
                        <th>Средняя температура</th>
                        <th>Атмосферное давление</th>
                        <th>Скорость ветра</th>
                        <th>Осадки</th>
                    </tr>
                    </thead>
                    <tbody className="text-center">
                    {weather.statistics.map(statistic =>
                        <tr key={statistic.id}>
                            <td>{statistic.date}</td>
                            <td>{statistic.minTemp}</td>
                            <td>{statistic.maxTemp}</td>
                            <td>{statistic.avgTemp}</td>
                            <td>{statistic.pressure}</td>
                            <td>{statistic.windSpeed}</td>
                            <td>{statistic.rainfall}</td>
                        </tr>
                    )}
                    </tbody>
                    <p></p>
                </Table>
            </Card>
        </Container>
    );
});

export default Archive;