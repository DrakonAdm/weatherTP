import React, {useContext} from 'react';
import {observer} from "mobx-react-lite";
import {Context} from "../index";
import {useNavigate} from "react-router-dom";
import {Button, Card, Col, Container, Dropdown, Form, Image, Row} from "react-bootstrap";
import {HOME_ROUTE} from "../utils/consts";

const ChangeAd = observer(() => {
    document.body.style.background = "#FFFAF4";

    const {data} = useContext(Context)

    return (
        <Container>
            <Row>
                <Col>
                    <Card style={{width: 500, backgroundColor: "#FFFAF4", borderWidth: 0}} className="p-4">
                        <Dropdown>
                            <Dropdown.Toggle variant="success" id="dropdown-basic">
                                Выберите страницу
                            </Dropdown.Toggle>
                            <Dropdown.Menu>
                                {data.pages.map(page =>
                                    <Dropdown.Item href="#/action-1">{page.page}</Dropdown.Item>
                                )}
                            </Dropdown.Menu>
                        </Dropdown>
                       <Image src={process.env.REACT_APP_API_URL + data.pages[0].image}/>
                    </Card>

                </Col>
                <Col>
                    <Card className="p-3" style={{width: 400, borderWidth: 0, backgroundColor: "#FFFAF4"}}>
                        <Button
                            variant={"outline-dark"}
                            className="mt-3 align-self-center button_menu align-items-center"
                        >
                            Загрузить новое изображение
                        </Button>
                        <Button
                            variant={"outline-dark"}
                            className="mt-3 align-self-center button_menu align-items-center"
                        >
                            Сохранить изменения
                        </Button>
                    </Card>
                </Col>
            </Row>
        </Container>
    );
});

export default ChangeAd;