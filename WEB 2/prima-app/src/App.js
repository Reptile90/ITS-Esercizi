import React from "react";
import ProfiloUtente from "./ProfiloUtente";
import Form from "./form"
import "bootstrap/dist/css/bootstrap.min.css";

function App() {
const utenti = [
    {
      id: 123456,
      nome: 'Stefano',
      cognome: 'Reali',
      eta: 34,
      professione: 'Sviluppatore Cloud',
      email: 'stefano.reali@mail.com',
    },
    {
      id: 151232,
      nome: 'Lorenzo',
      cognome: 'Anzivino',
      eta: 27,
      professione: 'Graphic Designer',
      email: 'lorenzo.anzivino@mail.com',
    },
    {
      id: 31235215,
      nome: 'Marcel',
      cognome: 'Movileanu',
      eta: 23,
      professione: 'Sviluppatore Cloud',
      email: 'marcel.movileanu@mail.com',
    },
        {
      id: 31233315,
      nome: 'Francesco',
      cognome: 'Magno',
      eta: 23,
      professione: 'Sviluppatore Cloud',
      email: 'marcel.movileanu@mail.com',
    }
  ];

  const arraySlice = [];
  for (let i = 0; i < utenti.length; i += 3) {
    arraySlice.push(utenti.slice(i, i + 3));
  }

  return (
    <div className="container mt-4">
      {arraySlice.map((gruppo, index) => (
        <div className="row mb-4" key={index}>
          {gruppo.map((utente) => (
            <div className="col-md-4" key={utente.id}>
              <ProfiloUtente utente={utente} />
            </div>
          ))}
        </div>
      ))}
      <Form></Form>
    </div>
  );
}



export default App;
