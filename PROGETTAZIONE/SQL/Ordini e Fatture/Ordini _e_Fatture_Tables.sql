
CREATE DOMAIN IntGEZ AS INTEGER
    CHECK (VALUE >= 0);

CREATE DOMAIN FloatGEZ AS FLOAT
    CHECK (VALUE >= 0);

CREATE DOMAIN Float01 AS FLOAT
    CHECK (VALUE >= 0 AND VALUE <= 1);


CREATE DOMAIN Stringa AS VARCHAR(100);


CREATE DOMAIN CodiceFiscale AS CHAR(16)
    CHECK (
        VALUE ~ '^[A-Z]{6}[0-9]{2}[A-Z][0-9]{2}[A-Z][0-9]{3}[A-Z]$'
    );


CREATE DOMAIN PartitaIva AS CHAR(11)
    CHECK (
        VALUE ~ '^[0-9]{11}$'
    );


CREATE DOMAIN Telefono AS VARCHAR
    CHECK (
        VALUE ~ '^\+[1-9][0-9]{7,14}$'
    );


CREATE DOMAIN Email AS VARCHAR
    CHECK(
        VALUE ~ '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
    );


CREATE TYPE Indirizzo AS (
  via Stringa,
  civico Stringa,
  CAP CHAR(5)
);


CREATE TYPE Stato AS ENUM(
    'in preparazione',
    'inviato',
    'da saldare'
);


CREATE TABLE Nazione(
    nome Stringa PRIMARY KEY
);

CREATE TABLE Regione(
    nome Stringa NOT NULL,
    nazione Stringa NOT NULL,
    PRIMARY KEY (nome),
    FOREIGN KEY (nazione) REFERENCES Nazione(nome)
);

CREATE TABLE Citta (
  nome Stringa NOT NULL,
  regione Stringa NOT NULL,
  nazione Stringa NOT NULL,
  PRIMARY KEY (nome, regione, nazione),
  FOREIGN KEY (regione) REFERENCES Regione(nome),
  FOREIGN KEY (nazione) REFERENCES Nazione(nome)
);

CREATE TABLE Direttore(
    nome Stringa NOT NULL,
    cognome Stringa NOT NULL,
    cf CodiceFiscale PRIMARY KEY,
    data_nascita DATE NOT NULL,
    anni_servizio IntGEZ NOT NULL,
    citta Stringa NOT NULL,
    regione Stringa NOT NULL,
    nazione Stringa NOT NULL,
    FOREIGN KEY (citta, regione, nazione) REFERENCES Citta(nome, regione, nazione)
);

CREATE TABLE Dipartimento (
    nome Stringa PRIMARY KEY,
    indirizzo Indirizzo NOT NULL,
    direttore CodiceFiscale,
    FOREIGN KEY (direttore) REFERENCES Direttore(cf)
);

CREATE TABLE Fornitore (
    ragione_sociale Stringa NOT NULL,
    partitaiva PartitaIva PRIMARY KEY,
    indirizzo Indirizzo NOT NULL,
    telefono Telefono NOT NULL,
    email Email NOT NULL
);

CREATE TABLE Ordine (
    id INTEGER PRIMARY KEY,
    data_stipula DATE NOT NULL,
    imponibile FloatGEZ NOT NULL,
    aliquotaiva Float01 NOT NULL,
    descrizione Stringa NOT NULL,
    stato Stato NOT NULL,
    fornitore PartitaIva NOT NULL,
    dipartimento Stringa NOT NULL,
    FOREIGN KEY (fornitore) REFERENCES Fornitore(partitaiva),
    FOREIGN KEY (dipartimento) REFERENCES Dipartimento(nome)
);




