import React, {useContext} from 'react';
import {Button, ButtonGroup, Card, CardGroup, Col, Container, Row} from "react-bootstrap";
import {DATE_ROUTE, DAYS_ROUTE, HOME_ROUTE, MONTH_ROUTE, TOMORROW_ROUTE} from "../utils/consts";
import DayItem from "../components/DayItem";
import {Context} from "../index";
import {observer} from "mobx-react-lite";

const Days = observer(() => {
    document.body.style.background = "#FFFAF4";
    const {weather} = useContext(Context)
    return (
        <Container>
            <Card style={{width: 1000, borderWidth: 0, backgroundColor: "#FFFAF4"}} className="p-4 d-flex">
                <h2>Прогноз погоды на 10 дней</h2>
                <ButtonGroup className="d-flex">
                    <Button className="button_menu" variant="outline-dark" href={HOME_ROUTE}>Сегодня</Button>
                    <Button className="button_menu" variant="outline-dark" href={TOMORROW_ROUTE}>Завтра</Button>
                    <Button className="button_menu_active" variant="outline-dark" href={DAYS_ROUTE}>На 10 дней</Button>
                    <Button className="button_menu" variant="outline-dark" href={MONTH_ROUTE}>На месяц</Button>
                    <Button className="button_menu" variant="outline-dark" href={DATE_ROUTE}>Дата</Button>
                </ButtonGroup>
            </Card>
            <Card style={{width: 1000, borderWidth: 0, backgroundColor: "#FFFAF4"}} className="p-4 d-flex">
                <Col>
                    <Row md={5} classname="d-flex">
                        {weather.weather.map(weather =>
                            <DayItem key={weather.id} weather={weather}/>
                        )}
                    </Row>
                </Col>
                {/*<Card style={{borderWidth: 0}} className="text-center">
                        <Card.Body>
                            <Card.Title>Ср 26.04.23</Card.Title>
                            <Card.Img variant="top" src="облака-дождь.png"/>
                            <Card.Text>
                                Дождь
                            </Card.Text>
                        </Card.Body>
                        <big className="align-self-center">+14</big>
                    </Card>*/}

            </Card>
        </Container>
    );
});

export default Days;