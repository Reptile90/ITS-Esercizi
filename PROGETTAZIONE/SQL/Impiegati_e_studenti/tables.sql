
create table posizionemilitare(
	nome stringa primary key
);

CREATE TABLE Persona (
    cf CodiceFiscale PRIMARY KEY,
    nome Stringa NOT NULL,
    cognome Stringa NOT NULL,
    data_nascita DATE NOT NULL,
    maternita IntGEZ,
    is_uomo BOOLEAN NOT NULL,
    is_donna BOOLEAN NOT NULL,
    pos_uomo Stringa,
    FOREIGN KEY (pos_uomo) REFERENCES PosizioneMilitare(nome),

    CHECK (
        (is_uomo = TRUE) = (pos_uomo IS NOT NULL)
    ),
    CHECK (
        (is_donna = TRUE) = (maternita IS NOT NULL)
    ),
    CHECK (
        is_uomo = TRUE OR is_donna = TRUE
    )
);


CREATE TABLE Studente (
    persona CodiceFiscale PRIMARY KEY,
    FOREIGN KEY (persona) REFERENCES Persona(cf),
    matricola IntGEZ NOT NULL,
    UNIQUE (matricola)
);


CREATE TABLE Impiegato (
    persona CodiceFiscale PRIMARY KEY,
    FOREIGN KEY (persona) REFERENCES Persona(cf),
    stipendio FloatGEZ NOT NULL,
    ruolo Ruolo NOT NULL
);

CREATE TABLE Progetto (
    id SERIAL PRIMARY KEY,
    nome Stringa NOT NULL,
    responsabile_progetto CodiceFiscale NOT NULL,
    FOREIGN KEY (responsabile_progetto) REFERENCES Impiegato(persona)
);

-- Vincoli non implementabili direttamente
-- 	nello schema relazionale:

-- [V.Impiegato.Progettista.responsabile]
--	Per ogni i:Impiegato
--	 se i è coinvolto in un link resp_prog
--	 allora i.ruolo = 'Progettista'