import React, {useContext} from 'react';
import {observer} from "mobx-react-lite";
import {Button, Card, CardGroup, Container, Table} from "react-bootstrap";
import {ABNORMAL_ROUTE, ARCHIVE_ROUTE} from "../utils/consts";
import {Context} from "../index";

const Abnormal = observer(() => {
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
                        className="button_menu"
                        href={ARCHIVE_ROUTE}
                    >
                        Статистика за прошедшие годы
                    </Button>
                </Card>
                <Card style={{width: 900, backgroundColor: "#FFFAF4", borderWidth: 0}} className="p-5">
                    <Button
                        variant={"outline-dark"}
                        className="button_menu_active"
                        href={ABNORMAL_ROUTE}
                    >
                        Статистика аномальной погоды
                    </Button>
                </Card>
            </CardGroup>
            <Card style={{width: 900, backgroundColor: "#FFFAF4"}} className="p-5">
                <Table bordered hover7 size="sm" >
                    <thead className="text-center">
                    <tr style={{backgroundColor: "#EFF8FF"}} >
                        <th>Минимальная температура</th>
                        <th>Максимальная температура</th>
                        <th>Наибольшее количество осадков</th>
                        <th>Наибольшая скорость ветра</th>
                    </tr>
                    </thead>
                    <tbody className="text-center">
                    {weather.abnormal.map(statistic =>
                        <tr key={statistic.id}>
                            <td>{statistic.minTemp}</td>
                            <td>{statistic.maxTemp}</td>
                            <td>{statistic.maxRainfall}</td>
                            <td>{statistic.maxWindSpeed}</td>
                        </tr>
                    )}
                    </tbody>
                    <p></p>
                </Table>
            </Card>
        </Container>
    );
});

export default Abnormal;