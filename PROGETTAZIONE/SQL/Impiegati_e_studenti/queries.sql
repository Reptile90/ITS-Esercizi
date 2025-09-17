--Quali sono i nomi degli impiegati nati a partire dall'anno?

select nome
from persona,impiegato
where  persona.cf = impiegato.persona
order by data_nascita asc;

--Quali sono i nomi di tutti i progetti?

select nome
from progetto;

--Quali sono gli stipendi dei direttori?
select stipendio
from impiegato
where ruolo = 'Direttore';

--Quanti sono i progettisti?
select count(*)
from impiegato
where ruolo = 'Progettista';

--Quanti sono i responsabili?
select count(*)
from impiegato,progetto
where impiegato.persona = resp_prog;


--Quanti sono i progettisti che non sono responsabili? 


--Qual è lo stipendio medio dei segretari?
SELECT AVG(stipendio)
FROM Impiegato
WHERE ruolo = 'Segretario';

--Qual è l'età della/o studente meno giovane?

    --usare select(date_part('year',age(current_date, <DATA DI NASCITA>))) as eta FROM [...];

SELECT max (DATE_PART('year', AGE(current_date, data_nascita))) AS eta
FROM Studente,Persona
where persona.cf = studente.persona;


--Quanti sono i direttori che hanno assolto agli obblighi militari?
select count(cf)
from persona, impiegato
where ruolo = 'Direttore' 
	and persona.cf = impiegato.persona 
	and persona.pos_uomo is not null;


--Quanti sono i progetti di cui è responsabile un'impiegata con almeno due figli?
select count(id)
from persona,progetto
where persona.maternita >= 2
	and persona.cf = progetto.resp_prog;

