import React from 'react';
import {Card, Col, Form, Row} from "react-bootstrap";

const DayItem = ({weather}) => {
    return (
        <Col>
            <Card style={{width: 150, cursor: 'pointer', backgroundColor: "#EFF8FF"}} border={"large"}>
               {/* <Card style={{borderWidth: 0}} className="text-center">*/}
                    <Card.Body>
                        <Card.Title>{weather.date}</Card.Title>
                        {/*<Card.Img variant="top" src="солнце.png"/> тут можно weather.image если хранить картинку в дне*/}
                        <Card.Text>
                            Днем: {weather.maxTemp} {""}
                            Ночью: {weather.minTemp}
                        </Card.Text>
                    </Card.Body>
                <Card.Footer>
                    <small className="align-self-center">Давление: {weather.pressure} {""} Скорость ветра: {weather.windSpeed} {""} Осадки: {weather.rainfall}</small>
                </Card.Footer>
{/*                </Card>*/}
            </Card>
        </Col>
    );
};

export default DayItem;