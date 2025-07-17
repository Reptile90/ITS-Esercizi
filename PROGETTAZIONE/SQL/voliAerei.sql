CREATE DOMAIN Stringa as varchar;
CREATE DOMAIN IntGEZ as integer
        check (value >= 0);
CREATE DOMAIN IntGZ as integer
        check (value > 0);
CREATE DOMAIN IntG1900 as integer
        check (value > 1900);

CREATE TABLE Nazione(
    id integer primary key,
    nome Stringa not null
);

CREATE TABLE Citta(
    id integer primary key,
    n_abitanti intGEZ not null,
    nome Stringa not null,
    nazione integer not null,

    foreign key (nazione) references Nazione(id)
);

CREATE TABLE Aereoporto(
    id integer primary key,
    nome Stringa not null,
    codice Stringa not null,
    citta integer not null,

    foreign key (citta) references Citta(id)
);

CREATE TABLE CompagniaAerea(
    id integer primary key,
    fondazione intG1900 not null,
    nome Stringa not null,
    citta integer not null,

    foreign key (citta) references Citta(id)
);

CREATE TABLE Volo(
    id integer primary key,
    codice Stringa not null,
    durata intGZ not null,
    compagniaAerea integer not null,
    aeroporto_partenza integer not null,
    aeroporto_arrivo integer not null,

    foreign key (compagniaAerea) references CompagniaAerea(id),
    foreign key (aeroporto_partenza) references Aereoporto(id),
    foreign key (aeroporto_arrivo) references Aereoporto(id)
);
