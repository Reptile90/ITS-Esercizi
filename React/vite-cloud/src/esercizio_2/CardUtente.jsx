import React from 'react';

const CardUtente = (props) => {
    const nome = props.nome;
    const email = props.email;
    const imgUrl = props.imgUrl;

    return (
        <div className='card m-3 shadow w-50'>
            <img src={imgUrl} className='card image-top img-fluid  ' alt="Avatar Utente" />
            <div className='card-body'></div>
            <h2 className='card-title text-primary'>{nome}</h2>
            <p className='card-text text-primary'>{email}</p>

        </div>
    );
};

export default CardUtente;
