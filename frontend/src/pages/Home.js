import React, {useContext} from 'react';
import {Button, ButtonGroup, Card, CardGroup, Container} from "react-bootstrap";
import {DATE_ROUTE, DAYS_ROUTE, HOME_ROUTE, MONTH_ROUTE, TOMORROW_ROUTE} from "../utils/consts";
import {observer} from "mobx-react-lite";
import {Context} from "../index";


const Home = observer(() => {
    document.body.style.background = "#FFFAF4";
    const {data} = useContext(Context);



    return (
        <Container>
            <Card style={{width: 1000, borderWidth: 0, backgroundColor: "#FFFAF4"}} className="p-4 d-flex">
                <h2>Прогноз погоды на сегодня</h2>
                <ButtonGroup className="d-flex">
                    <Button className="button_menu_active" variant="outline-dark" href={HOME_ROUTE}>Сегодня</Button>
                    <Button className="button_menu" variant="outline-dark" href={TOMORROW_ROUTE}>Завтра</Button>
                    <Button className="button_menu" variant="outline-dark" href={DAYS_ROUTE}>На 10 дней</Button>
                    <Button className="button_menu" variant="outline-dark" href={MONTH_ROUTE}>На месяц</Button>
                    <Button className="button_menu" variant="outline-dark" href={DATE_ROUTE}>Дата</Button>
                </ButtonGroup>
            </Card>
            <Card style={{width: 1000, borderWidth: 0, backgroundColor: "#FFFAF4"}} className="p-4 d-flex">
                <h3>{data.weather[1].date}</h3> {/*здесь как-то надо получать определенный день, чтобы для него уже выводить все*/}
                <CardGroup style={{width: 900}}>
                    <Card style={{borderWidth: 3, backgroundColor: "#EFF8FF"}} className="p-4 text-center">
                        <h3>Днем: {data.weather[1].maxTemp}</h3>
                        <h4>Ночью: {data.weather[1].minTemp}</h4>
                    </Card>
                    <Card style={{borderWidth: 3, backgroundColor: "#EFF8FF"}} className="p-4 text-center">
                        <h7>Давление: {data.weather[1].pressure}</h7>
                        <h7>Скорость ветра: {data.weather[1].windSpeed} </h7>
                        <h7>Осадки: {data.weather[1].rainfall}</h7>
                    </Card>
                </CardGroup>
                <Card style={{width: 900, borderWidth: 3, backgroundColor: "#EFF8FF"}} className="text-center">
                    <h4>Рекомендуемая одежда на день</h4>
                    <h5>{data.clothes}</h5>
                </Card>
            </Card>
        </Container>
    );
});

export default Home;