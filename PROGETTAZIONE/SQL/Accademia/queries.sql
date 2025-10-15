--1. Quanti sono gli strutturati di ogni fascia?
select posizione, count(posizione)
from persona as p
group by posizione

--2. Quanti sono gli strutturati con stipendio ≥ 40000?
select count(persona)
from persona
where stipendio >= 40000

--3. Quanti sono i progetti già finiti che superano il budget di 50000?

select count(*) as numero
from progetto as p
where p.budget > 50000
	and p.fine < current_date

--4. Qual è la media, il massimo e il minimo delle ore delle attività relative al progetto "Pegasus"

select avg(oredurata)as media, min(oredurata), max(oredurata)
from progetto as p, attivitaprogetto as a
where p.nome = 'Pegasus' and a.progetto = p.id


--5. Quali sono le medie, i massimi e i minimi delle ore giornaliere dedicate al progetto ‘Pegasus’ da ogni singolo docente?
select p.id,  p.nome, p.cognome , avg(oredurata) as media, min (oredurata) as minimo, max (oredurata) as massimo 
from persona as p, progetto as pr, attivitaprogetto as a
where pr.nome = 'Pegasus'
	and p.id = a.persona
		and a.progetto = pr.id
group by p.id, p.nome, p.cognome

--6. Qual è il numero totale di ore dedicate alla didattica da ogni docente?

select p.id, p.nome, p.cognome,  sum(oredurata) as ore_didattica
from persona as p, attivitaNonprogettuale as a
where p.id = a.persona
	and a.tipo = 'Didattica'
group by p.id, p.nome, p.cognome 

--7. Qual è la media, il massimo e il minimo degli stipendi dei ricercatori?

select avg(stipendio) as media_stipendio, min(stipendio) as minimo_stipendio, max(stipendio) as massimo_stipendio 
from persona
where posizione = 'Ricercatore'

--8. Quali sono le medie, i massimi e i minimi degli stipendi dei ricercatori, dei professori associati e dei professori ordinari?
select posizione,  avg(stipendio) as media_stipendios, max(stipendio) as massimo_stipendio, min(stipendio) as minimo_stipendio
from persona
group by posizione

--9. Quante ore ‘Ginevra Riva’ ha dedicato ad ogni progetto nel quale ha lavorato?

select pr.id as id_progetto, pr.nome as progetto, sum(a.oreDurata) AS totale_ore
from persona as p, progetto as pr,attivitaprogetto as a
where p.nome = 'Ginevra'
	and p.cognome = 'Riva'
	and a.persona = p.id
	and a.progetto = pr.id
group by pr.id

-- 10. Qual è il nome dei progetti su cui lavorano più di due strutturati?

select pr.id, pr.nome
from persona p, attivitaprogetto as a, progetto pr
where p.id = a.persona
	and a.progetto = pr.id
group by pr.id, pr.nome
having count(distinct p.id) > 2

--11 ) Quali sono i professori associati che hanno lavorato su piu ’ di un progetto ?

select p.id,p.nome,p.cognome
from persona as p, attivitaprogetto as a
where p.posizione ='Professore Associato'
	and a.persona = p.id
group by p.id, p.nome, p.cognome
having count(distinct a.progetto)> 1