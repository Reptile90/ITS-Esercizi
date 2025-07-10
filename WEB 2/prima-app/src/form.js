import React, { useState } from 'react';

const Form = () => {
  const [nome, setNome] = useState("");
  const [cognome, setCognome] = useState("");

  const gestioneDati = (e) => {
    e.preventDefault();
    if (nome && cognome) {
      setNome("");
      setCognome("");
      alert("Ciao");
    } else {
      alert("Per favore, compila tutti i campi.");
    }
  };

  return (
    <div className="container">
      <form className="row g-3" onSubmit={gestioneDati}>
        <div className="col-md-6">
          <label htmlFor="inputNome" className="form-label">Nome</label>
          <input
            type="text"
            value={nome}
            onChange={(e) => setNome(e.target.value)}
            className="form-control"
            id="inputNome"
          />
        </div>
        <div className="col-md-6">
          <label htmlFor="inputCognome" className="form-label">Cognome</label>
          <input
            type="text"
            value={cognome}
            onChange={(e) => setCognome(e.target.value)}
            className="form-control"
            id="inputCognome"
          />
        </div>
        <div className="col-12">
          <button type="submit" className="btn btn-primary">Invia</button>
        </div>
      </form>
    </div>
  );
};

export default Form;
