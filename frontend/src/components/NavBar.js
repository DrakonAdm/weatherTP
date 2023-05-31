import React, {useContext} from 'react';
import {Button, Container, Nav, Navbar, Form, NavDropdown} from "react-bootstrap";
import {NavLink, Route,BrowserRouter as Router, Routes} from "react-router-dom";
import {DISEASES_ROUTE, MEDICAMENTS_ROUTE, MAIN_ROUTE} from "../utils/consts";
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
                        <Button variant="outline-success">Найти</Button>
                    </Form>
                    {user.isAuth ?
                        <Nav className="ml-auto my-2 my-lg-0" style={{ maxHeight: '100px'}}>
                            <Nav.Link href="/">Главная</Nav.Link>
                            <Nav.Link href="/statistic">Статистика</Nav.Link>
                            <Nav.Link href="/profile">Личный кабинет</Nav.Link>
                        </Nav>
                        :
                        <Nav className="ml-auto my-2 my-lg-0" style={{ maxHeight: '100px'}}>
                            <Nav.Link href="/">Главная</Nav.Link>
                            <Nav.Link href="/statistic">Статистика</Nav.Link>
                            <Nav.Link href="/login">Войти</Nav.Link>
                        </Nav>
                    }
                    </Container>
            </Navbar>
        </>
    );
});

export default NavBar;