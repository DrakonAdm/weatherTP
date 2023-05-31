import React, {useContext} from 'react';
import {observer} from "mobx-react-lite";
import {Context} from "../index";
import {Pagination} from "react-bootstrap";

const Pages = observer(() => {
    const {medbox} = useContext(Context)
    const pageCount = Math.ceil(medbox.totalCount / medbox.limit)
    const pages = []
    for (let i = 0; i < pageCount; i++){
        pages.push(i + 1)
    }
    return (
        <Pagination className="mt-5">
            {pages.map(page =>
                <Pagination.Item
                    key={page}
                    active={medbox.page === page}
                    onClick={() => medbox.setPage(page)}
                >
                    {page}
                </Pagination.Item>
            )}
        </Pagination>
    );
});

export default Pages;