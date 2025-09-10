import React, { useState } from 'react'

const ModuloContatti = () => {
    const [dati, setDati] = useState({
        nome: "",
        email: "",
        messaggio: ""
    }
    );

    const handleChange = (e) => {
        const { name, value } = e.target;
        setDati(dati => ({
            ...dati,
            [name]: value
        }));
    };
      const handleSubmit = (e) => {
    e.preventDefault();
    console.log('Dati inviati:', dati);
      };
    return (
        
            <div className="container mt-5">
                <h2 className="mb-4">Modulo di Contatto</h2>
                <form onSubmit={handleSubmit}>
                    <div className="mb-3">
                        <label htmlFor="nome" className="form-label">Nome</label>
                        <input
                            type="text"
                            className="form-control"
                            id="nome"
                            name="nome"
                            value={dati.nome}
                            onChange={handleChange}
                            placeholder="Inserisci il tuo nome"
                        />
                    </div>
                    <div className="mb-3">
                        <label htmlFor="email" className="form-label">Email</label>
                        <input
                            type="email"
                            className="form-control"
                            id="email"
                            name="email"
                            value={dati.email}
                            onChange={handleChange}
                            placeholder="Inserisci la tua email"
                        />
                    </div>
                    <div className="mb-3">
                        <label htmlFor="messaggio" className="form-label">Messaggio</label>
                        <textarea
                            className="form-control"
                            id="messaggio"
                            name="messaggio"
                            rows="4"
                            value={dati.messaggio}
                            onChange={handleChange}
                            placeholder="Scrivi il tuo messaggio"
                        />
                    </div>
                    <button type="submit" className="btn btn-primary">Invia</button>
                </form>
            </div>
        );
    };
    export default ModuloContatti