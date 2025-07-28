CREATE DOMAIN IntGEZ AS INTEGER
    CHECK (VALUE >= 0);

CREATE DOMAIN FloatGEZ AS FLOAT
    CHECK (VALUE >= 0);
CREATE DOMAIN Float01 AS FLOAT
    CHECK (VALUE >= 0 AND VALUE<= 1)

CREATE DOMAIN Stringa as varchar(100);

CREATE DOMAIN CodiceFiscale AS CHAR(16);
    CHECK (VALUE ~'^[A-Z]{6}[0-9]{2}[A-Z][0-9]{2}[A-Z][0-9]{3}[A-Z]$');

CREATE DOMAIN PartitaIva AS CHAR(11)
    CHECK (VALUE ~ '^[0-9]{11}$');


CREATE DOMAIN Telefono AS VARCHAR
    CHECK (VALUE ~ '^\\+[1-9][0-9]{7,14}$');

CREATE DOMAIN Email AS VARCHAR
    CHECK(VALUE ~ '^[\w\.-]+@[\w\.-]+\.\w{2,}$')

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
    nome Stringa NOT NULL
    PRIMARY KEY (nome)
);

CREATE TABLE Regione(
    nome Stringa NOT NULL,
    PRIMARY KEY (NOME)
)
CREATE TABLE Citta (
    nome Stringa not null,
    PRIMARY KEY (nome)
    FOREIGN KEY ()
);


