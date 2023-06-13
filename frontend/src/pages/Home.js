import React, {useContext, useEffect} from 'react';
import {Button, ButtonGroup, Card, CardGroup, Col, Container, Image, Row} from "react-bootstrap";
import {DATE_ROUTE, DAYS_ROUTE, HOME_ROUTE, MONTH_ROUTE, TOMORROW_ROUTE} from "../utils/consts";
import {observer} from "mobx-react-lite";
import {Context} from "../index";
import {getAd, getClothes, getWeatherMain} from "../http/weatherApi";


const Home = observer(() => {

    const {data} = useContext(Context);
    const {user} = useContext(Context);

    useEffect(() => {
        getWeatherMain(user.chooseCity).then(day => data.setWeatherDay(day))
        getClothes().then(clothes => data.setClothes(clothes))
        getAd("mainPage").then(page => data.setPage(page))
    }, [])

    return (
        <div className="background">
        <Container>
            <Row>
                <Col md={9}>
                    <Card style={{width: 800, borderWidth: 0, backgroundColor: "transparent", }} className="p-4 d-flex">
                        <h2>Прогноз погоды на сегодня, {user.chooseCity} </h2>
                        <ButtonGroup className="mt-3 d-flex">
                            <Button className="button_menu_active" variant="outline-dark" href={HOME_ROUTE}>Сегодня</Button>
                            <Button className="button_menu" variant="outline-dark" href={TOMORROW_ROUTE}>Завтра</Button>
                            <Button className="button_menu" variant="outline-dark" href={DAYS_ROUTE}>На 5 дней</Button>
                            <Button className="button_menu" variant="outline-dark" href={DATE_ROUTE}>Дата</Button>
                        </ButtonGroup>
                    </Card>
                    <Card style={{width: 1000, borderWidth: 0, backgroundColor: "transparent"}} className="p-4 d-flex">
                        <h3>{data.weatherDay[0].date}</h3> {/*здесь как-то надо получать определенный день, чтобы для него уже выводить все*/}
                        <CardGroup style={{width: 900}}>
                            <Card style={{borderWidth: 3, backgroundColor: "#EFF8FF"}} className="p-4 text-center">
                                <h3>Днем: {data.weatherDay[0].maxTemp}</h3>
                                <h4>Ночью: {data.weatherDay[0].minTemp}</h4>
                            </Card>
                            <Card style={{borderWidth: 3, backgroundColor: "#EFF8FF"}} className="p-4 text-center">
                                <h7>Давление: {data.weatherDay[0].pressure}</h7>
                                <h7>Скорость ветра: {data.weatherDay[0].windSpeed} </h7>
                                <h7>Осадки: {data.weatherDay[0].rainfall}</h7>
                            </Card>
                        </CardGroup>
                        <Card style={{width: 900, borderWidth: 3, backgroundColor: "#EFF8FF"}}
                              className="p-1">
                            <h4 className="text-center">Рекомендуемая одежда</h4>
                            <h5>ㅤㅤ• на день в целом: {data.clothes[0]}</h5>
                            <h5>ㅤㅤ• днем: {data.clothes[1]}</h5>
                            <h5>ㅤㅤ• ночью: {data.clothes[2]}</h5>
                        </Card>
                    </Card>
                </Col>
                <Col>
                    <Card style={{left: 50, top: 130, height: 400, width:300, borderWidth: 0, backgroundColor: "transparent",}} className="align-items-center text-center">
                        <Card.Body>
                            <Card.Img width={300} height={400} src={process.env.REACT_APP_API_URL + data.page[0].image}/>
                        </Card.Body>
                    </Card>
                </Col>
            </Row>
        </Container>
        </div>
    );
});

export default Home;