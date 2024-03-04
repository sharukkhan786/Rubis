import React, { useState, useEffect } from 'react';

function MyComponent() {
    const [data, setData] = useState({
        "book_review":"Good book",
        "rating": 5,
        "book": 1
        });

    useEffect(() => {
        axios.post('http://localhost:8000/api/book_shop/review')  
            .then(response => {
                setData(response.data);
            })
            .catch(error => {
                console.error('Error fetching data:', error);
            });
    }, []); 

    return (
        <div>
            {}
            {data.map(item => (
                <div key={item.id}>
                    {}
                    <p>{item.name}</p>
                </div>
            ))}
        </div>
    );
}

function MyComponent_1() {
    const [data, setData] = useState([]);

    useEffect(() => {
        axios.get('http://localhost:8000/api/user/detail/1')  
            .then(response => {
                setData(response.data);
            })
            .catch(error => {
                console.error('Error fetching data:', error);
            });
    }, []); 

    return (
        <div>
            {}
            {data.map(item => (
                <div key={item.id}>
                    {}
                    <p>{item.name}</p>
                </div>
            ))}
        </div>
    );
}
export default MyComponent;
export default MyComponent_1;

