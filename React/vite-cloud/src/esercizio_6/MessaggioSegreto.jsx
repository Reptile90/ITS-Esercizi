import React, { useState } from 'react'

const MessaggioSegreto = () => {
    const [mostra,setMostra]= useState(false)
  return (
    <div>
        <button onClick={()=>setMostra(true)}>Mostra Messaggio</button>
        {mostra && <p>Messaggio Segreto</p>}
    </div>
  )
}

export default MessaggioSegreto