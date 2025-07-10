create type Strutturato as enum 
('Ricercatore', 'Professore Associato', 'Professore Ordinario');

create type LavoroProgetto as enum
('Ricerca e Sviluppo','Dimostrazione','Management', 'Altro');

create type LavoroNonProgettuale as enum 
('Didattica','Ricerca', 'Missione', 'Incontro Dipartimentale', 'Incontro Accademico','Altro');

create type CausaAssenza as enum 
('Chiusura Universitaria', 'Maternità', 'Malattia');

create domain PosInteger as integer
    check (value >= 0);

create domain StringaM as varchar(100);

create domain NumeroOre as PosInteger
    check (value <= 8);

create domain Denaro as real 
    check (value >= 0);


create table Persona (
    id PosInteger primary key,
    nome StringaM unique not null,
    cognome StringaM not null,
    posizione strutturato not null,
    stipendio Denaro not null
);

create table Progetto (
    id PosInteger primary key,
    nome StringaM not null,
    inizio date not null,
    fine date not null,
    budget Denaro not null,
    check (inizio < fine)
);

create table WP (
    progetto PosInteger,
    id PosInteger,
    nome StringaM not null,
    inizio date not null,
    fine date not null,
    primary key(progetto,id),
    unique(progetto,nome),
    check (inizio < fine),
    Foreign Key (progetto) REFERENCES Progetto(id)
);

create table AttivitaProgetto (
    id PosInteger primary key,
    persona PosInteger not null,
    progetto PosInteger not null,
    wp PosInteger not null,
    giorno date not null,
    tipo LavoroProgetto not null,
    oreDurata NumeroOre not null,
    Foreign Key (persona) REFERENCES Persona(id),
    Foreign Key (progetto,wp) REFERENCES WP(progetto,id)
);

create table AttivitaNonProgettuale (
    id PosInteger primary key,
    persona PosInteger not null,
    tipo LavoroNonProgettuale not null,
    giorno date not null,
    oreDurata NumeroOre not null,
    Foreign Key (persona) REFERENCES Persona(id)
);

create table Assenza(
    id PosInteger primary key,
    persona PosInteger not null,
    tipo CausaAssenza not null,
    giorno date not null,
    unique(persona,giorno),
    Foreign Key (persona) REFERENCES Persona(id)
);


