import React, {useContext, useEffect, useState} from 'react';
import {Button, Container, Form, FormControl, Nav, Navbar, OverlayTrigger, Popover} from "react-bootstrap";
import {useNavigate} from "react-router-dom";
import {HOME_ROUTE, LOGIN_ROUTE, PROFILE_USER_ROUTE, STATISTIC_ROUTE,} from "../utils/consts";
import {Context} from "../context";
import {observer} from "mobx-react-lite";
import '../components/App.css'
import {getListCity} from "../http/weatherApi";

const NavBar = observer( () => {
    const {user} = useContext(Context)
    const navigate = useNavigate();

    const [cities, setCities] = useState([]);
    const [searchValue, setSearchValue] = useState('');
    const [filteredCities, setFilteredCities] = useState([]);
    const [city, setCity] = useState('');

    useEffect(() => {
        async function fetchData() {
            try {
                const cityData = await getListCity();
                setCities(cityData);
                setFilteredCities(cityData);
            } catch (error) {
                console.error('Ошибка при получении списка городов:', error);
            }
        }

        fetchData();
    }, []);

    const handleSearchChange = (event) => {
        const value = event.target.value;
        setSearchValue(value);
        const filtered = cities.filter(city => city.startsWith(value));
        setFilteredCities(filtered);
    }

    const handleCityClick = (city) => {
        setCity(city);
        setSearchValue(city);
        setFilteredCities(cities);
    }

    const popover = (
        <Popover id="popover-basic">
            <ul style={{ listStyle: 'none', margin: 0, padding: 0, width: 120, maxHeight: 100, overflowY: 'scroll'}}>
                {filteredCities && filteredCities.map(city => (
                    <li key={city} style={{ backgroundColor: '#fff', padding: '5px', cursor: 'pointer' }} onClick={() => handleCityClick(city)}>
                        {city}
                    </li>
                ))}
            </ul>
        </Popover>
    );

    const searchClick = () => {
        user.setChooseCity(city);
        navigate(HOME_ROUTE);
    }

    return (
        <>
            <Navbar className='navbar-default'>
                <Container>
                    <Navbar.Brand href="/">Погода от Терминатора</Navbar.Brand>
                    <Navbar.Toggle aria-controls="navbarScroll" />
                    <Form className="d-flex">
                        <OverlayTrigger trigger="click" placement="bottom" overlay={popover}>
                            <FormControl
                                type="text"
                                placeholder="Найти город"
                                value={searchValue}
                                onChange={handleSearchChange}
                                className="m-1"
                            />
                        </OverlayTrigger>
                        <Button
                            variant="outline-dark"
                            disabled={city === ""}
                            onClick={searchClick}
                        >
                            Найти
                        </Button>
                    </Form>
                    {user.isAuth ?
                        <Nav className="ml-auto my-2 my-lg-0" style={{ maxHeight: '100px'}}>
                            <Nav.Link href={HOME_ROUTE}>Главная</Nav.Link>
                            <Nav.Link href={STATISTIC_ROUTE}>Статистика</Nav.Link>
                            <Nav.Link href={PROFILE_USER_ROUTE}>Личный кабинет</Nav.Link>
                        </Nav>
                        :
                        <Nav className="ml-auto my-2 my-lg-0" style={{ maxHeight: '100px'}}>
                            <Nav.Link href={HOME_ROUTE}>Главная</Nav.Link>
                            <Nav.Link href={STATISTIC_ROUTE}>Статистика</Nav.Link>
                            <Nav.Link href={LOGIN_ROUTE}>Войти</Nav.Link>
                        </Nav>
                    }
                    </Container>
            </Navbar>
        </>
    );
});

export default NavBar;