import React, {useContext, useEffect, useState} from 'react';
import {
    Button,
    Card,
    CardGroup,
    Col,
    Container,
    Dropdown,
    Form,
    OverlayTrigger,
    Row,
    Table,
    Tooltip
} from "react-bootstrap";
import {ABNORMAL_ROUTE, ARCHIVE_ROUTE, REGISTRATION_ROUTE,} from "../utils/consts";
import {observer} from "mobx-react-lite";
import {Context} from "../context";
import {getListCityCountry, getStatistic} from "../http/weatherApi";
import DropdownToggle from "react-bootstrap/DropdownToggle";
import DropdownMenu from "react-bootstrap/DropdownMenu";
import {utils, writeFile} from "xlsx";
import Pages from "../components/Pages";
import statistic from "./Statistic";


const Archive = observer(() => {
    document.body.style.background = "#FFFAF4";
    const {data, setData} = useContext(Context);
    const {user} = useContext(Context);

    const [nextPage, setNextPage] = useState(null);
    const [previousPage, setPreviousPage] = useState(null);

    const searchStat = () => {
        try {
            getStatistic(1, 10, country, city, date1, date2).then(day => {
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

    const exportToExcel = (tableData, fileName) => {
        const worksheet = utils.json_to_sheet(tableData);
        const workbook = utils.book_new();
        utils.book_append_sheet(workbook, worksheet, 'Sheet1');
        writeFile(workbook, fileName.toString() + ".xlsx");
    };


    const tooltip = (
        <Tooltip id="tooltip">
            Чтобы посмотреть статистику аномальной погоды, вам нужно войти или зарегистрироваться
        </Tooltip>
    );


    const isFormValid = () => {
        return city !== '' && country !== '' && date1 !== '' && date2 !== '';
    }

    return (
        <div className="background">
            <Container
                style={{height: window.innerHeight - 50, width: window.innerWidth - 250, backgroundColor: "transparent"}}
            >
                <Row>
                    <Col md={9}>
                        <CardGroup>
                            <Card style={{width: 900, backgroundColor: "transparent", borderWidth: 0}} className="p-5">
                                <Button
                                    variant={"outline-dark"}
                                    className="button_menu_active"
                                    href={ARCHIVE_ROUTE}
                                >
                                    Статистика за прошедшие годы
                                </Button>
                            </Card>
                            <Card style={{width: 900, backgroundColor: "transparent", borderWidth: 0}} className="p-5">
                                {user.isAuth ?
                                    <Button
                                        variant={"outline-dark"}
                                        className="button_menu"
                                        href={ABNORMAL_ROUTE}
                                    >
                                        Статистика аномальной погоды
                                    </Button>
                                    :
                                    <OverlayTrigger placement="right" overlay={tooltip}>
                                        <Button
                                            variant={"outline-dark"}
                                            className="button_menu"
                                            datatype="Подсказка"
                                            href={REGISTRATION_ROUTE}
                                        >
                                            Статистика аномальной погоды
                                        </Button>
                                    </OverlayTrigger>
                                }
                            </Card>
                        </CardGroup>
                        <Card style={{width: 900, backgroundColor: "transparent", borderWidth: 0}}>
                            <Row className="d-flex align-items-center justify-content-center">
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
                                        <DropdownToggle className="drop_menu" variant="outline-dark" style={{ width: 170 }}>
                                            {city || "Выберите город"}
                                        </DropdownToggle>
                                        <DropdownMenu style={{ maxHeight: '200px', overflowY: 'auto' }}>
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
                                        placeholder="Дата начала"
                                        type="date"
                                        min="2015-01-01"
                                        max={new Date().toISOString().split("T")[0]}
                                    /></Col>
                                <Col>
                                    <Form.Control
                                        value={date2}
                                        onChange={e => setDate2(e.target.value)}
                                        className="button-menu"
                                        placeholder="Дата окончания"
                                        type="date"
                                        min="2015-01-01"
                                        max={new Date().toISOString().split("T")[0]}
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
                                <Card style={{width: 900, backgroundColor: "transparent", borderWidth: 0}} className="mt-3">
                                    <Table bordered hover7 size="sm">
                                        <thead className="text-center">
                                        <tr style={{backgroundColor: "#EFF8FF"}}>
                                            <th style={{width: 100}}>Дата</th>
                                            <th>Минимальная температура</th>
                                            <th>Максимальная температура</th>
                                            <th>Средняя температура</th>
                                            <th>Атмосферное давление</th>
                                            <th>Скорость ветра</th>
                                            <th>Осадки</th>
                                        </tr>
                                        </thead>
                                        <tbody style={{backgroundColor: "#FFFAF4"}} className="text-center">
                                        {data.map(statistic =>
                                            <tr key={statistic.id}>
                                                <td>{statistic.date}</td>
                                                <td>{statistic.minTem}</td>
                                                <td>{statistic.maxTem}</td>
                                                <td>{statistic.averageTem}</td>
                                                <td>{statistic.atmosphericPressure}</td>
                                                <td>{statistic.windSpeed}</td>
                                                <td>{statistic.precipitation}</td>
                                            </tr>
                                        )}
                                        </tbody>
                                    </Table>
                                    <div className="pagination-buttons">
                                        <Button
                                            variant={"outline-dark"}
                                            className="pagination-button"
                                            onClick={() => paginationData(previousPage)}
                                            disabled={!previousPage}
                                        >
                                            Назад
                                        </Button>
                                        <Button
                                            variant={"outline-dark"}
                                            className="pagination-button"
                                            onClick={() => paginationData(nextPage)}
                                            disabled={!nextPage}
                                        >
                                            Вперёд
                                        </Button>
                                    </div>
                                    <p></p>
                                    <button className="button_menu"
                                            onClick={() => exportToExcel(data, "table")}>Сохранить таблицу в файл
                                        .xlsx
                                    </button>
                                </Card>
                        }
                    </Col>
                    <Col>
                        <Card style={{left: 50, top: 130, height: 450, borderWidth: 0, backgroundColor: "transparent",}}
                              className="align-items-center text-center">
                            <Card.Body>
                                <Card.Img width={250} height={400}
                                          src={`${process.env.REACT_APP_API_URL}advertisementGET/?short=statistic`}/>
                            </Card.Body>
                        </Card>
                    </Col>
                </Row>
            </Container>
        </div>
    );
});

export default Archive;