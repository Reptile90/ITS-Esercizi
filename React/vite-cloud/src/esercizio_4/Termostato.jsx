import { useState } from 'react'
import React from 'react'

const Termostato = () => {
    const [temperatura, setTemperatura] = useState(20);
    return (
        <div className="container mt-4 text-center">
            <h1 className='text-primary display-4'>TERMOSTATO</h1>
            <h2 classname="text-primary display-4">{temperatura}°C</h2>
            <button className="btn btn-success m-2" onClick={() => setTemperatura(temperatura + 1)}>
                Aumenta
            </button>
            <button className="btn btn-danger m-2" onClick={() => setTemperatura(temperatura - 1)}>
                Diminuisci

            </button>



        </div>
    )
}

export default Termostato