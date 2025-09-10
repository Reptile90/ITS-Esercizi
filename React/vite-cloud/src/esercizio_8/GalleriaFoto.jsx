import React, { useEffect, useState } from 'react'

const url = 'https://jsonplaceholder.typicode.com/photos?_limit=10'
const GalleriaFoto = () => {
  const [foto, setFoto] = useState([]);
  const [staCaricando, setStaCaricando] = useState(true);
  const [errore, setErrore] = useState(null);

  useEffect(() => {
    const caricaFoto = async () => {
      try {
        const response = await fetch(url);
        const dati = await response.json();
        setFoto(dati);
        setStaCaricando(false);
      } catch (err) {
        setErrore(err.message);
        setStaCaricando(false);
      }
    };

    caricaFoto();
  }, []);

  return (
    <div className="container mt-4 text-center">
      <h2> Galleria Foto</h2>

      {staCaricando && <p>Caricamento in corso...</p>}
      {errore && <p className="text-danger">Errore: {errore}</p>}

      {!staCaricando && !errore && (
        <div className="row">
          {foto.map((foto) => (
            <div key={foto.id} className="col-md-4 mb-4">
              <img
                src={foto.Url}
                alt={foto.title}
                className="img-fluid rounded shadow"
              />
              <p>{foto.title}</p>
            </div>
          ))}
        </div>
      )}
    </div>
  )
}

export default GalleriaFoto