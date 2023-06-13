import React, {useContext} from 'react';
import {observer} from "mobx-react-lite";
import {Context} from "../index";
import {Pagination} from "react-bootstrap";

const Pages = observer(() => {
    const {data} = useContext(Context)
    const pageCount = Math.ceil(data.statTotalCount / data.statLimit)
    const pages = []
    for (let i = 0; i < pageCount; i++){
        pages.push(i + 1)
    }
    return (
        <Pagination className="mt-3 align-self-center">
            {pages.map(page =>
                <Pagination.Item
                    key={page}
                    active={data.statPage === page}
                    onClick={() => data.setStatPage(page)}
                >
                    {page}
                </Pagination.Item>
            )}
        </Pagination>
    );
});

export default Pages;