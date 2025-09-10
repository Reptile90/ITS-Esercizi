import React, { useState } from 'react'

const CampoRicerca = () => {
    const [testoRicerca, setTestoRicerca] = useState("");
    return (
        <div className="display-4 text-center">
            <input 
            type="text" 
            value={testoRicerca} 
            onChange={(e)=> setTestoRicerca(e.target.value)} />
            <p>Stai cercando: {testoRicerca}</p>
        </div>
    )
}

export default CampoRicerca