import React, { useState } from 'react';

const Contatore = () => {
  const [count, setCount] = useState(0);
  const [valore, setValore] = useState(1); // valore di incremento personalizzato

  return (
    <div className="container mt-5">
      <div className="card text-center shadow">
        <div className="card-header bg-primary text-white">
          <h2>Contatore React</h2>
        </div>

        <div className="card-body">
          <h1 className="display-4">{count}</h1>

          <div className="mb-3">
            <label htmlFor="valore" className="form-label">Valore personalizzato:</label>
            <input
              type="number"
              id="valore"
              className="form-control w-25 mx-auto"
              value={valore}
              onChange={(e) => setValore(Number(e.target.value))}
              min="1"
            />
          </div>

          <div className="d-flex justify-content-center gap-3 flex-wrap mt-4">
            <button className="btn btn-primary" onClick={() => setCount(count + 1)}>+ AUMENTA</button>
            <button className="btn btn-danger" onClick={() => setCount(count - 1)}>- DIMINUISCI</button>
            <button className="btn btn-success" onClick={() => setCount(count + valore)}>+ AUMENTA DI {valore}</button>
            <button className="btn btn-dark" onClick={() => setCount(count - valore)}>- DIMINUISCI DI {valore}</button>
            <button className="btn btn-info" onClick={() => setCount(0)}>🔄 RESET</button>
          </div>
        </div>

        <div className="card-footer text-muted">
          Powered by useState 💙
        </div>
      </div>
    </div>
  );
};

export default Contatore;
