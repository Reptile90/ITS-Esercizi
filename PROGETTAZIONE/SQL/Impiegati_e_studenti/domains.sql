create domain stringa as varchar;

create domain IntGEZ as integer
    check(value >= 0);

create domain FloatGEZ as real  
    check(value >= 0);

create type Ruolo as enum(
    'Direttore','Segretario','Progettista'
);
CREATE DOMAIN CodiceFiscale AS VARCHAR(16)
    CHECK(VALUE  ~ '^[A-Z]{6}[0-9]{2}[A-Z]{1}[0-9]{2}[A-Z]{1}[0-9]{3}[A-Z]{1}$');