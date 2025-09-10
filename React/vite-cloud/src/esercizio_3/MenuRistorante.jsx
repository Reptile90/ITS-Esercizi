import React from 'react'
import piatti from './piatti'
const MenuRistorante = () => {
    return (
        <div className='container mt-4'>
            <h2>Menu del Ristorante</h2>
            <ul className='list-group'>
                {piatti.map((piatto) => (
                    <li key={piatto.id} className='list-group-item d-flex justify-content-between align-items-center'>
                        {piatto.nome}
                        <span className="badge bg-primary rounded-pill">
                            € {piatto.prezzo}
                        </span>
                    </li>
                ))}
            </ul>

        </div>

    );
};

export default MenuRistorante