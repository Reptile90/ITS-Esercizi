import React, { useState, useEffect } from "react";

const UserCrud = () => {
    const [persona, setPersona] = useState({
        id: "",
        name: "",
        lastname: "",
        email: "",
        phone_number: ""
    });

    const [persone, setPersone] = useState([]);

    // Carica i dati da localStorage al primo render
    useEffect(() => {
        const storedPersone = localStorage.getItem("persone");
        if (storedPersone) {
            setPersone(JSON.parse(storedPersone));
        }
    }, []);

    // Salva i dati su localStorage ogni volta che cambia la lista
    useEffect(() => {
        localStorage.setItem("persone", JSON.stringify(persone));
    }, [persone]);

    const handler = (e) => {
        const { name, value } = e.target;
        setPersona({ ...persona, [name]: value });
    };

    const gestioneDati = (e) => {
        e.preventDefault();
        const { id, name, lastname, email, phone_number } = persona;

        if (id && name && lastname && email && phone_number) {
            setPersone([...persone, persona]);
            setPersona({
                id: "",
                name: "",
                lastname: "",
                email: "",
                phone_number: ""
            });
        } else {
            alert("Compila tutti i campi!");
        }
    };

    const eliminaPersona = (idToDelete) => {
        const nuovaLista = persone.filter(p => p.id !== idToDelete);
        setPersone(nuovaLista);
    };

    return (
        <div className="container mt-5">
            <div className="row justify-content-center">
                <div className="col-md-8 col-lg-6">
                    <form className="p-4 border rounded shadow bg-white" onSubmit={gestioneDati}>
                        <h4 className="mb-4 text-center">User Information</h4>

                        <div className="form-group mb-3">
                            <label htmlFor="inputID">ID</label>
                            <input
                                type="text"
                                className="form-control"
                                id="inputID"
                                name="id"
                                placeholder="Enter ID"
                                value={persona.id}
                                onChange={handler}
                            />
                        </div>

                        <div className="form-group mb-3">
                            <label htmlFor="inputName">Name</label>
                            <input
                                type="text"
                                className="form-control"
                                id="inputName"
                                name="name"
                                placeholder="Enter Name"
                                value={persona.name}
                                onChange={handler}
                            />
                        </div>

                        <div className="form-group mb-3">
                            <label htmlFor="inputLastName">Last Name</label>
                            <input
                                type="text"
                                className="form-control"
                                id="inputLastName"
                                name="lastname"
                                placeholder="Enter Last Name"
                                value={persona.lastname}
                                onChange={handler}
                            />
                        </div>

                        <div className="form-group mb-3">
                            <label htmlFor="inputEmail">Email</label>
                            <input
                                type="email"
                                className="form-control"
                                id="inputEmail"
                                name="email"
                                placeholder="Enter Email"
                                value={persona.email}
                                onChange={handler}
                            />
                        </div>

                        <div className="form-group mb-4">
                            <label htmlFor="inputPhoneNumber">Phone Number</label>
                            <input
                                type="tel"
                                className="form-control"
                                id="inputPhoneNumber"
                                name="phone_number"
                                placeholder="Enter Phone Number"
                                value={persona.phone_number}
                                onChange={handler}
                            />
                        </div>

                        <button type="submit" className="btn btn-primary w-100">
                            SUBMIT
                        </button>
                    </form>
                </div>
            </div>

            {persone.length > 0 && (
                <div className="row justify-content-center mt-5">
                    <div className="col-md-10">
                        <h5 className="mb-3">Lista Utenti</h5>
                        <ul className="list-group">
                            {persone.map((p, index) => (
                                <li key={index} className="list-group-item d-flex justify-content-between align-items-center">
                                    <span>
                                        <strong>ID:</strong> {p.id} | <strong>Nome:</strong> {p.name} {p.lastname} | <strong>Email:</strong> {p.email} | <strong>Telefono:</strong> {p.phone_number}
                                    </span>
                                    <button className="btn btn-danger btn-sm" onClick={() => eliminaPersona(p.id)}>
                                        Elimina
                                    </button>
                                </li>
                            ))}
                        </ul>
                    </div>
                </div>
            )}
        </div>
    );
};

export default UserCrud;




