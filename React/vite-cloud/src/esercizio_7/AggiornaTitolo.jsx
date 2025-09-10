import React, { useState } from 'react'
import { useEffect } from 'react'

const AggiornaTitolo = () => {
    const [nome,setNome]= useState("")

    useEffect(() => {document.title = nome ? `Ciao, ${nome}!` : "Benvenuto!"
  }, [nome]);
  return (
    <div>
      <h1>Aggiorna Titolo</h1>
      <input
        type="text"
        value={nome}
        onChange={(e) => setNome(e.target.value)}
        placeholder="Scrivi il tuo nome"
      />
    </div>
  )
}

export default AggiornaTitolo