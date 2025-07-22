


CREATE DOMAIN PosInteger as integer
        check(value >= 0);

CREATE DOMAIN StringaM as varchar(100);

CREATE DOMAIN CodIATA as char(3);

CREATE TABLE Compagnia(
    nome StringaM NOT NULL,
    annofondazione PosInteger,
    PRIMARY KEY (nome)
);

CREATE TABLE Aeroporto(
    codice CodIATA NOT NULL,
    nome StringaM NOT NULL,
    PRIMARY KEY (codice)
);

CREATE TABLE LuogoAeroporto(
    aeroporto CodIATA NOT NULL,
    citta StringaM NOT NULL,
    nazione StringaM NOT NULL,
    PRIMARY KEY (aeroporto),
    Foreign Key (aeroporto) REFERENCES Aeroporto(codice) DEFERRABLE
);



CREATE TABLE ArrPart(
    codice PosInteger,
    comp StringaM,
    arrivo CodIATA NOT NULL,
    partenza CodIATA NOT NULL,
    PRIMARY KEY (codice, comp),
    FOREIGN KEY (arrivo) REFERENCES Aeroporto(codice) , 
    FOREIGN KEY (partenza) REFERENCES Aeroporto(codice)
);

CREATE TABLE Volo(
    codice PosInteger,
    comp StringaM,
    durataMinuti PosInteger NOT NULL,
    PRIMARY KEY (codice, comp),
    FOREIGN KEY (comp) REFERENCES Compagnia(nome),
    FOREIGN KEY (codice, comp) REFERENCES ArrPart(codice, comp)DEFERRABLE
);

ALTER TABLE Aeroporto
ADD CONSTRAINT LuogoAeroportoFK Foreign Key (codice) REFERENCES LuogoAeroporto(aeroporto) DEFERRABLE;

ALTER TABLE ArrPart
ADD CONSTRAINT VoloCompagniaFK Foreign Key (codice, comp) REFERENCES Volo(codice, comp) DEFERRABLE;






