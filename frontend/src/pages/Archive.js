import React from 'react';
import {Card, Container, Table} from "react-bootstrap";

const Archive = () => {
    return (
        <Container
            style={{height: window.innerHeight - 50, width: window.innerWidth - 500}}
        >
        <Card style={{width: 900} } className="p-5" >
        <Table striped bordered hover7 size="sm">
            <thead>
            <tr>
                <th>Дата</th>
                <th>Минимальная температура</th>
                <th>Максимальная температура</th>
                <th>Средняя температура</th>
                <th>Атмосферное давление</th>
                <th>Скорость ветра</th>
                <th>Осадки</th>
            </tr>
            </thead>
            <tbody>
            </tbody>
            <p> </p>
        </Table>
        </Card>
        </Container>
    );
};

export default Archive;