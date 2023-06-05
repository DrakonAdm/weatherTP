import React, {useContext} from 'react';
import {observer} from "mobx-react-lite";
import {Context} from "../index";
import {Button, Card, Container, Table} from "react-bootstrap";
import {USERS_ROUTE} from "../utils/consts";

const Users = observer ( () => {
    document.body.style.background = "#FFFAF4";
    const {data} = useContext(Context)
    return (
        <Container>
            <Card style={{width: 1000, backgroundColor: "#FFFAF4", borderWidth: 0}} className="p-4">
                <h3>Список пользователей</h3>
                <Button
                    variant={"outline-dark"}
                    className="button_menu"
                    href={USERS_ROUTE}
                >
                    Сохранить в файл
                </Button>
                <Card style={{width: 900, backgroundColor: "#FFFAF4", borderWidth: 0}} className="p-5">
                    <Table bordered hover7 size="sm" >
                        <thead className="text-center">
                        <tr style={{backgroundColor: "#EFF8FF"}} >
                            <th>Имя</th>
                            <th>Почта</th>
                        </tr>
                        </thead>
                        <tbody className="text-center">
                        {data.listUsers.map(user =>
                            <tr key={user.id}>
                                <td>{user.name}</td>
                                <td>{user.email}</td>
                            </tr>
                        )}
                        </tbody>
                    </Table>
                </Card>
            </Card>
        </Container>
    );
});

export default Users;