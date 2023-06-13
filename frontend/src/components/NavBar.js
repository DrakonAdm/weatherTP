import React, {useContext, useState} from 'react';
import {Button, Container, Nav, Navbar, Form, NavDropdown, Popover, OverlayTrigger, FormControl} from "react-bootstrap";
import {NavLink, Route, BrowserRouter as Router, Routes, useNavigate, useHref} from "react-router-dom";
import {
    HOME_ROUTE,
    STATISTIC_ROUTE,
    LOGIN_ROUTE,
    PROFILE_USER_ROUTE, ARCHIVE_ROUTE,
} from "../utils/consts";
import {Context} from "../index";
import {observer}  from "mobx-react-lite";
import '../components/App.css'

const NavBar = observer( () => {
    const {user} = useContext(Context)
    const {data} = useContext(Context)
    const {history} = useNavigate();

    const cities = data.listCities;

    const [searchValue, setSearchValue] = useState('');
    const [filteredCities, setFilteredCities] = useState(cities);
    const [city, setCity] = useState('');

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
            <ul style={{ listStyle: 'none', margin: 0, padding: 0, width: 100, maxHeight: 80, overflowY: 'scroll'}}>
                {filteredCities.map(city => (
                    <li key={city} style={{ backgroundColor: '#fff', padding: '5px', cursor: 'pointer' }} onClick={() => handleCityClick(city)}>
                        {city}
                    </li>
                ))}
            </ul>
        </Popover>
    );

    const searchClick = () => {
        user.setChooseCity(city);
        history.navigate(HOME_ROUTE);
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
                        {/*<Form.Control
                            type="search"
                            placeholder="Найти город"
                            className="me-2"
                            aria-label="Search"
                            value={searchValue}
                            onChange={(event) => setSearchValue(event.target.value)}
                        />*/}
                       {/*<Form.Floating>
                           {data.city
                               .filter((city) =>
                                   city.city.toLowerCase().includes(searchValue.toLowerCase())
                               )
                               .map((city) => (
                                   <li key={city.id}>{city.city}</li>
                               ))}
                       </Form.Floating>*/}
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