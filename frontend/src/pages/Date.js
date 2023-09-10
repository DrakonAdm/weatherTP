import React, {useContext, useEffect, useState} from 'react';
import {Button, ButtonGroup, Card, CardGroup, Col, Container, Form, Row} from "react-bootstrap";
import {DATE_ROUTE, DAYS_ROUTE, HOME_ROUTE, MONTH_ROUTE, TOMORROW_ROUTE} from "../utils/consts";
import {observer} from "mobx-react-lite";
import {Context} from "../context";
import {getAd, getClothes, getDate, getDate5, getStatistic, getWeatherDate} from "../http/weatherApi";
import Loader from "../components/Loader/Loader";

const Date = observer(() => {
    document.body.style.background = "#FFFAF4";
    const {data, setData} = useContext(Context);
    const {user} = useContext(Context);
    const [selectedDate, setSelectedDate] = useState(getDate());

    const formattedDate = getDate();
    const [date, setDate] = useState(formattedDate)

    useEffect(() => {
        getWeatherDate(date, user.chooseCity).then(day => {
            setData(day.data.results[0])
        });
    }, [])

    return (
        <div className="background">
            {
                Object.keys(data).length === 0 ? <Loader/>
                    :
                    <Container>
                        <Row>
                            <Col md={9}>
                                <Card style={{width: 800, borderWidth: 0, backgroundColor: "transparent"}} className="p-4 d-flex">
                                    <h2>Прогноз погоды на {data?.date}, {data?.city__city}</h2>
                                    <ButtonGroup className="mt-3 d-flex">
                                        <Button className="button_menu" variant="outline-dark"
                                                href={HOME_ROUTE}>Сегодня</Button>
                                        <Button className="button_menu" variant="outline-dark"
                                                href={TOMORROW_ROUTE}>Завтра</Button>
                                        <Button className="button_menu" variant="outline-dark" href={DAYS_ROUTE}>На 5
                                            дней</Button>
                                        <Button className="button_menu_active" variant="outline-dark"
                                                href={DATE_ROUTE}>Дата</Button>
                                    </ButtonGroup>
                                </Card>
                                <Card style={{width: 1000, borderWidth: 0, backgroundColor: "transparent"}} className="p-4 d-flex">
                                    <Form className="d-flex">
                                        <Form.Control
                                            value={selectedDate !== 0 ? selectedDate : date}
                                            onChange={e => {
                                                const newDate = e.target.value;
                                                setSelectedDate(newDate);
                                                getWeatherDate(e.target.value, user.chooseCity).then(day => {
                                                setData(day.data.results[0])
                                            })}
                                            }
                                            className="button-menu"
                                            placeholder="Дата начала"
                                            style={{width: 150}}
                                            type="date"
                                            min={getDate()}
                                            max={getDate5()}
                                        />
                                        {/*<Button className="button_menu" variant="outline-dark" style={{width:150}} onClick={search}>Найти</Button>*/}
                                    </Form>
                                    <CardGroup style={{width: 900}}>
                                        <Card style={{borderWidth: 3, backgroundColor: "#EFF8FF"}}
                                              className="p-4 mt-3 text-center">
                                            {/*<Card.Img variant="top" src="солнце.png" />*/}
                                            <h3>Днем: {data?.maxTem}</h3>
                                            <h4>Ночью: {data?.minTem}</h4>
                                        </Card>
                                        <Card style={{borderWidth: 3, backgroundColor: "#EFF8FF"}}
                                              className="p-4 mt-3 text-center">
                                            <h7>Давление: {data?.atmosphericPressure}</h7>
                                            <h7>Скорость ветра: {data?.windSpeed} </h7>
                                            <h7>Осадки: {data?.precipitation}</h7>
                                        </Card>
                                    </CardGroup>
                                    <Card style={{width: 900, borderWidth: 3, backgroundColor: "#EFF8FF"}}
                                          className="p-1">
                                        <h4 className="text-center">Рекомендуемая одежда</h4>
                                        <h5>ㅤㅤ• на день в целом: {data?.averageClothes}</h5>
                                        <h5>ㅤㅤ• днем: {data?.maxClothes}</h5>
                                        <h5>ㅤㅤ• ночью: {data?.minClothes}</h5>
                                    </Card>
                                </Card>
                            </Col>
                            <Col>
                                <Card style={{left: 50, top: 200, height: 450, backgroundColor: "transparent", borderWidth: 0}}
                                      className="align-items-center text-center">
                                    <Card.Body>
                                        <Card.Img width={250} height={400}
                                                  src={`${process.env.REACT_APP_API_URL}advertisementGET/?short=date`}/>
                                    </Card.Body>
                                </Card>
                            </Col>
                        </Row>
                    </Container>
            }
        </div>
    );
});

export default Date;