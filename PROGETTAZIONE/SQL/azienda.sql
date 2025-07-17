CREATE DOMAIN Stringa as varchar;
CREATE DOMAIN Denaro as float
    check(value >= 0);

create table Dipartimento(
    id integer primary key,
    nome Stringa not null, 
    telefono Stringa not null 

);

create table Impiegato(
    id integer primary key, 
    nome Stringa not null, 
    data_nascita date not null,
    stipendio Denaro not null,
    dirige integer not null,
    afferisce integer not null ,
    data_afferenza date not null,
    Foreign Key (afferisce) REFERENCES Dipartimento(id)
   
);

create table Progetto(
    id integer primary key,
    nome Stringa not null,
    budget Denaro not null
    
);