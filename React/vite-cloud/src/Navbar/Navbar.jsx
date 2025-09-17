import React, { useState } from 'react'
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

const Navbar = () => {
    const lista_esercizi = ["Saluto","CardUtente","MenuRistorante","Termostato","CampoRicerca","MessaggioSegreto","AggiornaTitolo","GalleriaFoto","ModuloContatti","BlogApp","TodoApp"]

    const [esercizio,setEsercizio]= useState('')

    return (
        <div>
            <nav className="navbar navbar-expand-lg bg-body-tertiary">
  <div className="container-fluid">
    <a className="navbar-brand" href="#">
      Navbar w/ text
    </a>
    <button
      className="navbar-toggler"
      type="button"
      data-bs-toggle="collapse"
      data-bs-target="#navbarText"
      aria-controls="navbarText"
      aria-expanded="false"
      aria-label="Toggle navigation"
    >
      <span className="navbar-toggler-icon" />
    </button>
    <div className="collapse navbar-collapse" id="navbarText">
      <ul className="navbar-nav me-auto mb-2 mb-lg-0">
        {lista_esercizi.map((item) => (
        <li className="nav-item">

          <button onClick={()=> {setEsercizio(item)}}></button>
        </li>))}
        <li className="nav-item">
          <a className="nav-link" href="#">
            Features
          </a>
        </li>
        <li className="nav-item">
          <a className="nav-link" href="#">
            Pricing
          </a>
        </li>
      </ul>
      <span className="navbar-text">Navbar text with an inline element</span>
    </div>
  </div>
</nav>
        </div>
    )
}

export default Navbar