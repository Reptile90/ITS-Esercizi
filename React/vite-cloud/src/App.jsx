import { useState } from 'react'
import './App.css'
import UserAlbums from './UserAlbums'
import Saluto from './esercizio_1/Saluto'
import CardUtente from './esercizio_2/CardUtente'
import MenuRistorante from './esercizio_3/MenuRistorante'
import Termostato from './esercizio_4/Termostato'
import CampoRicerca from './esercizio_5/CampoRicerca'
import MessaggioSegreto from './esercizio_6/MessaggioSegreto'
import AggiornaTitolo from './esercizio_7/AggiornaTitolo'
import GalleriaFoto from './esercizio_8/GalleriaFoto'
import ModuloContatti from './esercizio_9/ModuloContatti'
import BlogApp from './esercizio_10/BlogApp'
import TodoApp from './esercizio_11/TodoApp'

function App() {

    return (

        <>
            <Saluto/>
            <CardUtente nome = "Stefano" email = "stefano.reali1990@gmail.com" imgUrl="https://images.unsplash.com/flagged/photo-1575555201693-7cd442b8023f?q=80&w=1632&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"/>
            <MenuRistorante></MenuRistorante>
            <Termostato></Termostato>
            <CampoRicerca></CampoRicerca>
            <MessaggioSegreto></MessaggioSegreto>
            <AggiornaTitolo></AggiornaTitolo>
            <></>
            <GalleriaFoto></GalleriaFoto>
            <ModuloContatti></ModuloContatti>
            <BlogApp></BlogApp>
            <TodoApp></TodoApp>


        </>

    )
}

export default App
