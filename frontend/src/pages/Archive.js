import React, {useContext} from 'react';
import {Button, ButtonGroup, Card, CardGroup, Container, Dropdown, Table} from "react-bootstrap";
import {
    ABNORMAL_ROUTE,
    ARCHIVE_ROUTE,
    DATE_ROUTE,
} from "../utils/consts";
import {observer} from "mobx-react-lite";
import {Context} from "../index";

const Archive = observer(() => {
    document.body.style.background = "#FFFAF4";
    const {weather} = useContext(Context);
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
            <ButtonGroup className="d-flex">
                <Dropdown>
                    <Dropdown.Toggle id="dropdown-basic" className="button_menu" variant="outline-dark">
                        Выберите страну
                    </Dropdown.Toggle>
                    <Dropdown.Menu>
                        <Dropdown.Item href="#/action-1">Action</Dropdown.Item>
                        <Dropdown.Item href="#/action-2">Another action</Dropdown.Item>
                        <Dropdown.Item href="#/action-3">Something else</Dropdown.Item>
                    </Dropdown.Menu>
                </Dropdown>
                <Dropdown>
                    <Dropdown.Toggle id="dropdown-basic" className="button_menu" variant="outline-dark">
                        Выберите город
                    </Dropdown.Toggle>
                    <Dropdown.Menu>
                        <Dropdown.Item href="#/action-1">Action</Dropdown.Item>
                        <Dropdown.Item href="#/action-2">Another action</Dropdown.Item>
                        <Dropdown.Item href="#/action-3">Something else</Dropdown.Item>
                    </Dropdown.Menu>
                </Dropdown>
                <Button className="button_menu" variant="outline-dark" href={DATE_ROUTE}>Дата</Button>
            </ButtonGroup>
            <Card style={{width: 900, backgroundColor: "#FFFAF4"}} className="p-5">
                <Table bordered hover7 size="sm" >
                    <thead className="text-center">
                    <tr style={{backgroundColor: "#EFF8FF"}} >
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