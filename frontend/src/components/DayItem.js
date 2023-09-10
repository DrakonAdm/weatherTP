import React from 'react';
import {Card, Col, Form, Row} from "react-bootstrap";

const DayItem = ({weather, name}) => {
    return (
        <Col className={name === "month" ? "colStyle mt-2" : "colStyle2 mt-2"}>
            <Card style={{width: 150, cursor: 'pointer', backgroundColor: "#EFF8FF"}} border={"large"}>
               {/* <Card style={{borderWidth: 0}} className="text-center">*/}
                    <Card.Body>
                        <Card.Title>{weather?.date}</Card.Title>
                        {/*<Card.Img variant="top" src="солнце.png"/> тут можно weather.image если хранить картинку в дне*/}
                        <Card.Text>
                            Днем: {weather?.maxTem} {""}
                            Ночью: {weather?.minTem}
                        </Card.Text>
                    </Card.Body>
                <Card.Footer>
                    <small className="align-self-center">Давление: {weather?.atmosphericPressure} {""} Скорость ветра: {weather?.windSpeed} {""} Осадки: {weather?.precipitation}</small>
                </Card.Footer>
{/*                </Card>*/}
            </Card>
        </Col>
    );
};

export default DayItem;
