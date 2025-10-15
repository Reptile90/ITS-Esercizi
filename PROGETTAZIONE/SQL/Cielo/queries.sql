
--1. Quante sono le compagnie che operano (sia in arrivo che in partenza) nei diversi aeroporti?
select ae.codice, ae.nome,  count(distinct ar.comp) as numero_compagnia
from aeroporto as ae, arrpart as ar
where ae.codice = ar.arrivo
	or ae.codice = ar.partenza
group by ae.codice, ae.nome

--2. Quanti sono i voli che partono dall’aeroporto ‘HTR’ e hanno una durata di almeno 100 minuti?
select *
from volo as vl, arrpart as ar
where vl.codice = ar.codice
	and ar.partenza = 'HTR'
	and vl.durataminuti >= 100

--3. Quanti sono gli aeroporti sui quali opera la compagnia ‘Apitalia’, per ogni nazione nella quale opera?
select la.nazione, count(distinct la.aeroporto)as conteggio_aeroporti
from arrpart as ar, luogoaeroporto as la
where ar.comp = 'Apitalia'
	and (ar.partenza = la.aeroporto or ar.arrivo = la.aeroporto)
group by la.nazione

--4. Qual è la media, il massimo e il minimo della durata dei voli effettuati dalla compagnia ‘MagicFly’ ?
select avg(durataminuti) as durata_media, min(durataminuti) as durata_minima, max(durataminuti) as durata_massima
from volo 
where comp = 'MagicFly'


--5. Qual è l’anno di fondazione della compagnia più vecchia che opera in ognuno degli aeroporti?
select ae.codice, ae.nome, min(annofondazione) as anno
from compagnia as co, arrpart as ar, aeroporto as ae
where (ar.arrivo = ae.codice or ar.partenza = ae.codice)
	and ar.comp = co.nome
group by ae.codice, ae.nome

--6. Quante sono le nazioni (diverse) raggiungibili da ogni nazione tramite uno o più voli?
select lu.nazione as nazione, count(distinct la.nazione) as nazioni_raggiungibili
from arrpart ar, luogoaeroporto lu, luogoaeroporto la
where lu.nazione <> la.nazione
	and ar.partenza = lu.aeroporto
	and ar.arrivo = la.aeroporto
group by lu.nazione;

--7. Qual è la durata media dei voli che partono da ognuno degli aeroporti?
select ae.codice, ae.nome, avg(distinct durataminuti) as durata_media
from volo as vl, aeroporto as ae, arrpart as ar
where ar.partenza = ae.codice
	and ar.codice = vl.codice
	and ar.comp = vl.comp
group by ae.codice, ae.nome

--8. Qual è la durata complessiva dei voli operati da ognuna delle compagnie fondate a partire dal 1950?
select vl.comp as compagnia, sum(durataminuti) as durata_complessiva
from volo as vl, compagnia as co
where co.annofondazione >= 1950
	and vl.comp = co.nome
group by vl.comp

--9. Quali sono gli aeroporti nei quali operano esattamente due compagnie?
select ae.codice, ae.nome
from aeroporto as ae, arrpart as ar
where ar.partenza = ae.codice
	or ar.arrivo = ae.codice
group by ae.codice, ae.nome
having count(distinct ar.comp ) = 2

--10. Quali sono le città con almeno due aeroporti?
select citta
from luogoaeroporto 
group by citta
having count(*) >= 2
--11. Qual è il nome delle compagnie i cui voli hanno una durata media maggiore di 6 ore?
select comp
from volo as vl
group by comp
having avg(durataminuti) > 360

--12. Qual è il nome delle compagnie i cui voli hanno tutti una durata maggiore di 100 minuti?
select comp
from volo
group by comp
having min(durataminuti) > 100




--esempio con with mi creo una tabella temporanea che mi permette di confrontare la durata massima con un altra durata massima

with D as(
	select max(durataminuti) as max_durata
	from volo)
select comp
from volo, D
group by comp, D.max_durata
having max(durataminuti) > D.max_durata

--Qual'è il nome delle compagnie che non hanno alcun volo?
with D as 
	(select distinct ap.comp
	from volo as v, arrpart as ap
	where ap.codice = v.codice
	and ap.comp = v.comp)

select c.nome
from compagnia as c
group by c.nome
having c.nome not in (select * from D)