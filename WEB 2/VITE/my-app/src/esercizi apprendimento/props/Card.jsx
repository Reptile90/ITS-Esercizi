import React from 'react'

function Card({title, immagine, descrizione}) {

    return (
        <div className="card" style={{ width: "18rem" }}>
            <img src={immagine} className="card-img-top" alt="..." />
            <div className="card-body">
                <h2>{title}</h2>
                <p className="card-text">
                    {descrizione}
                </p>
            </div>
        </div>

    )
}

export default Card