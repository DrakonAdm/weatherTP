import React, {useContext, useEffect, useState} from 'react';
import {Button, ButtonGroup, Card, CardGroup, Col, Container, Image, Row} from "react-bootstrap";
import {DATE_ROUTE, DAYS_ROUTE, HOME_ROUTE, MONTH_ROUTE, TOMORROW_ROUTE} from "../utils/consts";
import {observer} from "mobx-react-lite";
import {Context} from "../context";
import {getAd, getClothes, getWeatherMain} from "../http/weatherApi";
import Loader from "../components/Loader/Loader";

const Home = observer(() => {
    const {data, setData} = useContext(Context);
    const {user} = useContext(Context);

    useEffect(() => {
        getWeatherMain(user.chooseCity).then(day => {
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
                              <Card style={{width: 800, borderWidth: 0, backgroundColor: "transparent", }} className="p-4 d-flex">
                                  <h2>Прогноз погоды на сегодня, {data?.city__city} </h2>
                                  <ButtonGroup className="mt-3 d-flex">
                                      <Button className="button_menu_active" variant="outline-dark" href={HOME_ROUTE}>Сегодня</Button>
                                      <Button className="button_menu" variant="outline-dark" href={TOMORROW_ROUTE}>Завтра</Button>
                                      <Button className="button_menu" variant="outline-dark" href={DAYS_ROUTE}>На 5 дней</Button>
                                      <Button className="button_menu" variant="outline-dark" href={DATE_ROUTE}>Дата</Button>
                                  </ButtonGroup>
                              </Card>
                              {data
                                && <Card style={{width: 1000, borderWidth: 0, backgroundColor: "transparent"}} className="p-4 d-flex">
                                    {/*<h3>{data?.weatherDay[0]?.date}</h3> /!*здесь как-то надо получать определенный день, чтобы для него уже выводить все*!/*/}
                                    <CardGroup style={{width: 900}}>
                                        <Card style={{borderWidth: 3, backgroundColor: "#EFF8FF"}} className="p-4 text-center">
                                            <h3>Днем: {data?.maxTem}</h3>
                                            <h4>Ночью: {data?.minTem}</h4>
                                        </Card>
                                        <Card style={{borderWidth: 3, backgroundColor: "#EFF8FF"}} className="p-4 text-center">
                                            <h6>Давление: {data?.atmosphericPressure}</h6>
                                            <h6>Скорость ветра: {data?.windSpeed} </h6>
                                            <h6>Осадки: {data?.precipitation}</h6>
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
                              }
                          </Col>
                          <Col>
                              <Card style={{left: 50, top: 130, height: 400, width:300, borderWidth: 0, backgroundColor: "transparent",}} className="align-items-center text-center">
                                  <Card.Body>
                                      <Card.Img width={300} height={400} src={`${process.env.REACT_APP_API_URL}advertisementGET/?short=main`}/>
                                  </Card.Body>
                              </Card>
                          </Col>
                      </Row>
                  </Container>
            }

        </div>
    );
});

export default Home;