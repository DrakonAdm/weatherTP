import React, {useContext, useEffect, useState} from 'react';
import {observer} from "mobx-react-lite";
import {Button, Card, CardGroup, Col, Container, Dropdown, Form, Row, Table} from "react-bootstrap";
import {ABNORMAL_ROUTE, ARCHIVE_ROUTE} from "../utils/consts";
import {Context} from "../context/index.js";
import {getAbnormal, getListCityCountry, getStatistic} from "../http/weatherApi";
import DropdownToggle from "react-bootstrap/DropdownToggle";
import DropdownMenu from "react-bootstrap/DropdownMenu";
import DropdownItem from "react-bootstrap/DropdownItem";
import {utils, writeFile} from "xlsx";

const Abnormal = observer(() => {
    document.body.style.background = "#FFFAF4";
    const {data, setData} = useContext(Context);
    const {user} = useContext(Context);

    const [nextPage, setNextPage] = useState(null);
    const [previousPage, setPreviousPage] = useState(null);

    const searchStat = () => {
        try {
            getAbnormal(1, 10, country, city, date1, date2).then(day => {
                setData(day.data.results)
                setNextPage(day.data.next);
            });
        } catch (e) {
            alert(e.response.data.message)
        }
    }

    const paginationData = async (url) => {
        try {
            if (url) {
                const response = await fetch(url);
                if (!response.ok) {
                    throw new Error(`HTTP error! Status: ${response.status}`);
                }
                const dataRes = await response.json(); // Parse response body as JSON
                setData(dataRes.results);
                setNextPage(dataRes.next);
                setPreviousPage(dataRes.previous);
            }
        } catch (error) {
            console.error('Error fetching data:', error);
        }
    };

    const [date1, setDate1] = useState('')
    const [date2, setDate2] = useState('')
    const [country, setCountry] = useState('')
    const [city, setCity] = useState('')

    const [listCityCountry, setListCityCountry] = useState([]);

    useEffect(() => {
        async function fetchData() {
            try {
                const list = await getListCityCountry();
                setListCityCountry(list);
            } catch (error) {
                console.error('Ошибка при получении списка стран и городов:', error);
            }
        }

        fetchData();
    }, []);


    const countries = [...new Set((listCityCountry).map(item => item.country))];

    const handleCountrySelect = (eventKey) => {
        const selectedCountry = eventKey;
        setCountry(selectedCountry);
    }

    const handleCitySelect = (eventKey) => {
        const selectedCity = eventKey;
        setCity(selectedCity);
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
                                    {listCityCountry
                                        .filter(city => city.country === country)
                                        .map(city => city.city)
                                        .map(item => (
                                            <Dropdown.Item
                                                key={item}
                                                eventKey={item}
                                                onClick={e => setCity(item)}
                                                onSelect={handleCitySelect}
                                            >
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
                                min="2015"
                                max={new Date().getFullYear().toString()}
                            /></Col>
                        <Col>
                            <Form.Control
                                value={date2}
                                onChange={e => setDate2(e.target.value)}
                                className="button-menu"
                                style={{width: 150}}
                                placeholder="Год окончания"
                                type="number"
                                min="2015"
                                max={new Date().getFullYear().toString()}
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
                {
                    Object.keys(data).length === 0 ? null
                        :
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
                                    {data.map(statistic =>
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
                }
            </Container>
        </div>
    );
});

export default Abnormal;