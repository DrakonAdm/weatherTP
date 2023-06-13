import React, {useContext, useEffect} from 'react';
import {Button, ButtonGroup, Card, CardGroup, Col, Container, Row} from "react-bootstrap";
import {DATE_ROUTE, DAYS_ROUTE, HOME_ROUTE, MONTH_ROUTE, TOMORROW_ROUTE} from "../utils/consts";
import DayItem from "../components/DayItem";
import {Context} from "../index";
import {observer} from "mobx-react-lite";
import {getAd, getWeather5Days} from "../http/weatherApi";

const Days = observer(() => {
    document.body.style.background = "#FFFAF4";
    const {data} = useContext(Context)
    const {user} = useContext(Context)

    useEffect(() => {
        getWeather5Days("days", user.chooseCity).then(days => data.setWeather5Days(days))
        getAd("daysPage").then(page => data.setPage(page))
    }, [])

    return (
        <div className="background">
            <Container>
                <Row>
                    <Col md={9}>
                        <Card style={{width: 800, borderWidth: 0, backgroundColor: "transparent"}} className="p-4 d-flex">
                            <h2>Прогноз погоды на 10 дней, {user.chooseCity}</h2>
                            <ButtonGroup className="mt-3 d-flex">
                                <Button className="button_menu" variant="outline-dark"
                                        href={HOME_ROUTE}>Сегодня</Button>
                                <Button className="button_menu" variant="outline-dark"
                                        href={TOMORROW_ROUTE}>Завтра</Button>
                                <Button className="button_menu_active" variant="outline-dark" href={DAYS_ROUTE}>На 5
                                    дней</Button>
                                <Button className="button_menu" variant="outline-dark" href={DATE_ROUTE}>Дата</Button>
                            </ButtonGroup>
                        </Card>
                        <Card style={{width: 1000, borderWidth: 0, backgroundColor: "transparent"}} className="p-4 d-flex">
                            <Col>
                                <Row md={9} classname="d-flex">
                                    {data.weather5Days.map(weather =>
                                        <DayItem key={weather.id} weather={weather} name={"days"}/>
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
                    </Col>
                    <Col>
                        <Card style={{left: 50, top: 130, height: 450, backgroundColor: "transparent", borderWidth: 0}}
                              className="align-items-center text-center">
                            <Card.Body>
                                <Card.Img width={250} height={400}
                                          src={process.env.REACT_APP_API_URL + data.page[0].image}/>
                            </Card.Body>
                        </Card>
                    </Col>
                </Row>
            </Container>
        </div>
    );
});

export default Days;