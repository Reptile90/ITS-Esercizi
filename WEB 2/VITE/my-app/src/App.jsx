import { useState } from 'react'
import './App.css'
import UserAlbums from './UserAlbums'
import Card from './esercizi apprendimento/props/Card'
import Navbar from './esercizi apprendimento/props/Navbar'

function App() {

  return (
    <>
    <Navbar></Navbar>
      <UserAlbums></UserAlbums>
      <div className='container' style={{ display: 'flex', gap: '1rem' }}>
        <Card title='Roma' immagine='https://images.unsplash.com/photo-1555992828-ca4dbe41d294?q=80&w=764&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D' descrizione="Roma, la Città Eterna, è un affascinante intreccio di storia, arte e vita quotidiana. Fondata oltre 2.700 anni fa, ospita monumenti iconici come il Colosseo, il Pantheon e la Basilica di San Pietro, immersi in un'atmosfera unica che mescola il passato glorioso con il dinamismo moderno. Una passeggiata a Roma è come viaggiare nel tempo — con un buon caffè tra le mani, ovviamente. "></Card>
        <Card title="Los Angeles" immagine='https://images.unsplash.com/photo-1503891450247-ee5f8ec46dc3?q=80&w=687&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D' descrizione='Los Angeles, spesso chiamata "la città degli angeli", è una metropoli vibrante sulla costa della California, celebre per il suo clima soleggiato, le spiagge iconiche come Santa Monica e Venice, e ovviamente Hollywood — il cuore pulsante dell’industria cinematografica. È un mosaico di culture, street art, cucina internazionale e quartieri dalle atmosfere uniche, dove ogni angolo ha la sua storia da raccontare.'></Card>
        <Card title='Tokyo' immagine='https://plus.unsplash.com/premium_photo-1661914240950-b0124f20a5c1?q=80&w=1470&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D' descrizione="Tokyo è una metropoli ultramoderna che pulsa di energia e contrasti affascinanti. Dai templi antichi di Asakusa ai grattacieli futuristici di Shibuya e Shinjuku, la città fonde tradizione e innovazione in modo unico. È famosa per la sua cultura pop, la cucina raffinata, i quartieri tematici come Akihabara e Harajuku, e una rete ferroviaria così efficiente da sembrare magia. Ogni angolo di Tokyo racconta una storia — e spesso lo fa con stile impeccabile"></Card>
        <Card title='Pechino' immagine='https://images.unsplash.com/photo-1603120527222-33f28c2ce89e?q=80&w=754&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D' descrizione=" Pechino, conosciuta anche come Beijing, è la capitale della Cina e una delle città più antiche e affascinanti del mondo. Situata nel nord del paese, è un centro politico, culturale e tecnologico con oltre 21 milioni di abitanti.
         La sua storia millenaria include dinastie imperiali, monumenti iconici come la Città Proibita, il Tempio del Cielo, il Palazzo d’Estate e tratti spettacolari della Grande Muraglia"></Card>
         <Card title='Giza' immagine='https://plus.unsplash.com/premium_photo-1694475367746-526db5575bb4?q=80&w=1477&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D' descrizione=" Giza è una città egiziana situata sulla riva occidentale del Nilo, a pochi chilometri dal Cairo. È celebre in tutto il mondo per ospitare uno dei siti archeologici più iconici della storia: la Necropoli di Giza, che include le tre grandi piramidi di Cheope, Chefren e Micerino, oltre alla maestosa Grande Sfinge"></Card></div>

    </>
  )
}

export default App
