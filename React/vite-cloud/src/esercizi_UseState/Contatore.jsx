import React, { useState } from 'react'

const Contatore = () => {
    const[numero,setNumero]=useState(0)
  return (
    <div>Contatore
        <div>
            <h1>{numero}
                <button onClick={setNumero(numero+1)}>Aumenta

                </button>
                <button onClick={setNumero(numero-1)}>Diminuisci

                </button>

            </h1>

        </div>



    </div>
  )
}

export default Contatore