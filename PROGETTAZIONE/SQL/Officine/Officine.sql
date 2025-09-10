CREATE TYPE Indirizzo AS (
  via Stringa,
  civico Stringa,
  CAP CHAR(5)
);

CREATE TYPE tipoPersona AS ENUM(
    'Staff',
    'Proprietario'
);

CREATE TYPE tipoStaff AS ENUM(
    'Direttore',
    'Dipendente'
);


CREATE DOMAIN Stringa AS VARCHAR(255);

CREATE DOMAIN Reale as REAL
    CHECK(VALUE >=0);

CREATE DOMAIN Reale1 as REAL 
    CHECK(VALUE >= 0 AND VALUE < 1);

CREATE DOMAIN IntGEZ AS INTEGER
    CHECK(VALUE >= 0);

CREATE DOMAIN CodiceFiscale AS VARCHAR(16)
    CHECK(VALUE  ~ '^[A-Z]{6}[0-9]{2}[A-Z]{1}[0-9]{2}[A-Z]{1}[0-9]{3}[A-Z]{1}$');

CREATE DOMAIN Telefono AS VARCHAR(20)
    CHECK ( VALUE ~ '^(\+|[0-9]+)?[0-9\s-()]{6,14}$' );

CREATE DOMAIN PartitaIva AS VARCHAR(11)
    CHECK ( VALUE ~ '^[0-9]{11}$' );

CREATE DOMAIN Email AS VARCHAR(255)
    CHECK ( VALUE ~ '^[A-Za-z0-9._%-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$' );

CREATE DOMAIN DataNascita AS DATE;

CREATE DOMAIN Orario AS TIME;


REATE TABLE Persona (
  cf CodiceFiscale PRIMARY KEY,
  nome Stringa NOT NULL,
  via Stringa NOT NULL,
  civico Stringa NOT NULL,
  CAP CHAR(5) NOT NULL,
  numeroTelefono Telefono NOT NULL,
  tipo_persona tipoPersona NOT NULL,
  tipo_staff tipoStaff,
  data_nascita DataNascita,
  inizioServizio DATE
