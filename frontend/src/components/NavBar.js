import React, {useContext} from 'react';
import {Button, Container, Nav, Navbar, Form, NavDropdown} from "react-bootstrap";
import {NavLink, Route,BrowserRouter as Router, Routes} from "react-router-dom";
import {
    HOME_ROUTE,
    STATISTIC_ROUTE,
    LOGIN_ROUTE,
    PROFILE_USER_ROUTE, PROFILE_ADMIN_ROUTE
} from "../utils/consts";
import {Context} from "../index";
import {observer}  from "mobx-react-lite";
import '../components/App.css'

const NavBar = observer( () => {
    const {user} = useContext(Context)
    return (
        <>
            <Navbar className='navbar-default'>
                <Container>
                    <Navbar.Brand href="/">Погода от Терминатора</Navbar.Brand>
                    <Navbar.Toggle aria-controls="navbarScroll" />
                    <Form className="d-flex">
                        <Form.Control
                            type="search"
                            placeholder="Найти город"
                            className="me-2"
                            aria-label="Search"
                        />
                        <Button variant="outline-dark">Найти</Button>
                    </Form>
                    {user.isAuth ?

                        <Nav className="ml-auto my-2 my-lg-0" style={{ maxHeight: '100px'}}>
                            <Nav.Link href={HOME_ROUTE}>Главная</Nav.Link>
                            <Nav.Link href={STATISTIC_ROUTE}>Статистика</Nav.Link>
                            {user.isAdmin ?
                                <Nav.Link  href={PROFILE_ADMIN_ROUTE}>Личный кабинет</Nav.Link>
                                :
                                <Nav.Link href={PROFILE_USER_ROUTE}>Личный кабинет</Nav.Link>
                            }
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