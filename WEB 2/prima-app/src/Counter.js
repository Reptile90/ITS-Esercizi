import React from 'react'
import { useState } from 'react';

function Counter() {
    const [count, setCount] = useState(0);

    const aumenta = () => setCount(count + 1);
    const diminuisci = () => setCount(count - 1)
return (
    <div className="container text-center mt-5" >
        <div className="card bg-primary text-warning p-5 shadow-lg rounded">
            <h1 className="mb-3">CONTATORE</h1>
            <h2 className="display-4">{count}</h2>
            <div className="mt-4 d-flex justify-content-center gap-3">
                <button className="btn btn-warning" onClick={diminuisci}>
                    Diminuisci
                </button>
                <button className="btn btn-success" onClick={aumenta}>
                    Aumenta
                </button>
            </div>
        </div>
    </div>
);


}
export default Counter;

//<React.StrictMode>
    //<Counter></Counter>


  //</React.StrictMode>
