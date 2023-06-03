import React, {useContext} from 'react';
import {observer} from "mobx-react-lite";
import {Button, Card, Container} from "react-bootstrap";
import {CHANGE_AD_ROUTE, HOME_ROUTE, USERS_ROUTE} from "../utils/consts";
import {Context} from "../index";

const ProfileAdmin = observer ( () => {
    document.body.style.background = "#FFFAF4";
    const {user} = useContext(Context)
    return (
        <Container>
            <Card style={{width: 1000, backgroundColor: "#FFFAF4", borderWidth: 0}} className="p-4">
                <h3>Личный кабинет администратора</h3>
                <h4>/имя/</h4>
                <Card style={{width: 900, backgroundColor: "#FFFAF4", borderWidth: 0}} className="p-5">
                    <Button
                        variant={"outline-dark"}
                        className="button_menu"
                        href={CHANGE_AD_ROUTE}
                    >
                        Редактор рекламы
                    </Button>
                </Card>
                <Card style={{width: 900, backgroundColor: "#FFFAF4", borderWidth: 0}} className="p-5">
                    <Button
                        variant={"outline-dark"}
                        className="button_menu"
                        href={USERS_ROUTE}
                    >
                        Список пользователей
                    </Button>
                </Card>
            </Card>
            <Button
                variant={"outline-dark"}
                className="button_menu"
                href={HOME_ROUTE}
            >
                Выйти
            </Button> {/*тут как то прописать логику выхода из лк*/}
        </Container>
    );
});

export default ProfileAdmin;