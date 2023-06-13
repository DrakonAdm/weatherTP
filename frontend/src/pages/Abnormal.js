import React, {useContext, useEffect, useState} from 'react';
import {observer} from "mobx-react-lite";
import {Button, Card, CardGroup, Col, Container, Dropdown, Form, Row, Table} from "react-bootstrap";
import {ABNORMAL_ROUTE, ARCHIVE_ROUTE} from "../utils/consts";
import {Context} from "../index";
import {getAbnormal, getStatistic} from "../http/weatherApi";
import DropdownToggle from "react-bootstrap/DropdownToggle";
import DropdownMenu from "react-bootstrap/DropdownMenu";
import DropdownItem from "react-bootstrap/DropdownItem";
import {utils, writeFile} from "xlsx";

const Abnormal = observer(() => {
    document.body.style.background = "#FFFAF4";
    const {data} = useContext(Context);

    const [date1, setDate1] = useState('')
    const [date2, setDate2] = useState('')
    const [country, setCountry] = useState('')
    const [city, setCity] = useState('')
    const countries = [...new Set(data.cityCountry.map(item => item.country))];

    /*
        useEffect(() => {
            getAbnormal(country, city, date1, date2).then(stat => data.setAbnormal(stat))
        }, [])
    */
    const handleCountrySelect = (eventKey) => {
        const selectedCountry = eventKey;
        setCountry(selectedCountry);
    }

    const handleCitySelect = (eventKey) => {
        const selectedCity = eventKey;
        setCity(selectedCity);
    }

    const searchStat = () => {
        getAbnormal(country, city, date1, date2).then(stat => data.setAbnormal(stat))
    }

    const isFormValid = () => {
        return city !== '' && country !== '' && date1 !== '' && date2 !== '';
    }

    const exportToExcel = (tableData, fileName) => {
        const worksheet = utils.json_to_sheet(tableData);
        const workbook = utils.book_new();
        utils.book_append_sheet(workbook, worksheet, 'Sheet1');
        writeFile(workbook, fileName.toString() + ".xlsx");
    };


    return (
        <div className="background">
            <Container
                style={{height: window.innerHeight - 50, width: window.innerWidth - 500, backgroundColor: "transparent"}}
            >
                <CardGroup>
                    <Card style={{width: 900, backgroundColor: "transparent", borderWidth: 0}} className="p-5">
                        <Button
                            variant={"outline-dark"}
                            className="button_menu"
                            href={ARCHIVE_ROUTE}
                        >
                            Статистика за прошедшие годы
                        </Button>
                    </Card>
                    <Card style={{width: 900, backgroundColor: "transparent", borderWidth: 0}} className="p-5">
                        <Button
                            variant={"outline-dark"}
                            className="button_menu_active"
                            href={ABNORMAL_ROUTE}
                        >
                            Статистика аномальной погоды
                        </Button>
                    </Card>
                </CardGroup>
                <Card style={{width: 900, backgroundColor: "transparent", borderWidth: 0}}
                      className="d-flex align-items-center justify-content-center">
                    <Row>
                        <Col>
                            <Dropdown>
                                <DropdownToggle className="drop_menu" variant="outline-dark"
                                                style={{width: 170,}}>{country || "Выберите страну"}</DropdownToggle>
                                <DropdownMenu>
                                    {countries.map(item => (
                                        <Dropdown.Item key={item} eventKey={item} onClick={(e) => {
                                            setCountry(item);
                                            setCity("");
                                        }} onSelect={handleCountrySelect}>
                                            {item}
                                        </Dropdown.Item>
                                    ))}
                                </DropdownMenu>
                            </Dropdown>
                        </Col>
                        <Col>
                            <Dropdown>
                                <DropdownToggle className="drop_menu" variant="outline-dark"
                                                style={{width: 170,}}>{city || "Выберите город"}</DropdownToggle>
                                <DropdownMenu>
                                    {data.cityCountry.filter(city => city.country === country).map(city => city.city).map(item => (
                                        <Dropdown.Item key={item} eventKey={item} onClick={e => setCity(item)}
                                                       onSelect={handleCitySelect}>
                                            {item}
                                        </Dropdown.Item>
                                    ))}
                                </DropdownMenu>
                            </Dropdown>
                        </Col>
                        <Col>
                            <Form.Control
                                value={date1}
                                onChange={e => setDate1(e.target.value)}
                                className="button-menu"
                                style={{width: 150}}
                                placeholder="Год начала"
                                type="number"
                                min="2020"
                                max="2023"
                            /></Col>
                        <Col>
                            <Form.Control
                                value={date2}
                                onChange={e => setDate2(e.target.value)}
                                className="button-menu"
                                style={{width: 150}}
                                placeholder="Год окончания"
                                type="number"
                                min="2020"
                                max="2023"
                            />
                        </Col>
                        <Col>
                            <Button
                                variant={"outline-dark"}
                                className="p-2 align-self-center"
                                style={{width: 150, height: 40, fontSize: 12,}}
                                onClick={() => searchStat()}
                                disabled={!isFormValid()}
                            >
                                Показать статистику
                            </Button>
                        </Col>
                    </Row>
                </Card>
                <Card style={{width: 900, backgroundColor: "transparent", borderWidth: 0}} className="p-5">
                    <Table bordered hover7 size="sm">
                        <thead className="text-center">
                        <tr style={{backgroundColor: "#EFF8FF"}}>
                            <th>Минимальная температура</th>
                            <th>Максимальная температура</th>
                            <th>Наибольшее количество осадков</th>
                            <th>Наибольшая скорость ветра</th>
                        </tr>
                        </thead>
                        <tbody className="text-center" style={{backgroundColor: "#FFFAF4"}}>
                        {data.abnormal.map(statistic =>
                            <tr key={statistic.id}>
                                <td>{statistic.min_tem}</td>
                                <td>{statistic.max_tem}</td>
                                <td>{statistic.precipitation}</td>
                                <td>{statistic.max_wind_speed}</td>
                            </tr>
                        )}
                        </tbody>
                        <p></p>
                    </Table>
                    <button className="button_menu"
                            onClick={() => exportToExcel(data.statistics, "table")}>Сохранить таблицу в файл
                        .xlsx
                    </button>
                </Card>
            </Container>
        </div>
    );
});

export default Abnormal;