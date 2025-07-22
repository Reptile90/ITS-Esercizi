--1. Quali sono i voli (codice e nome della compagnia) la cui durata supera le 3 ore?

select distinct codice,comp
from volo
where durataMinuti > 180;

-- 2 ) Quali sono le compagnie che hanno voli che superano le 3 ore ?

select distinct nome
from compagnia as c, volo as v
where c.nome = v.comp
	and durataMinuti > 180;
	
-- 3) Quali sono i voli ( codice e nome della compagnia ) che partono dall ’aeroporto con codice ’ CIA ’ 

select distinct *
from arrpart as ap
where ap.partenza = 'CIA';

--4 ) Quali sono le compagnie che hanno voli che arrivano all ’ aeroporto con codice ’FCO’ ?

select distinct comp
from arrpart as ap
where ap.arrivo = 'FCO';



--5 ) Quali sono i voli ( codice e nome della compagnia ) che partono dall ’aeroporto ’FCO ’ e arrivano all ’ aeroporto ’ JFK ’ ?

select distinct codice,comp
from arrpart as ap
where ap.partenza = 'FCO' 
	and ap.arrivo = 'JFK';
	
--6) Quali sono le compagnie che hanno voli che partono dall ’ aeroporto ’FCO ’ e atterrano all ’ aeroporto ’ JFK ’ ?

select distinct comp
from arrpart as ap
where ap.partenza = 'FCO'
	and ap.arrivo = 'JFK';
	
-- 7) Quali sono i nomi delle compagnie che hanno voli diretti dalla citta ’ di’ Roma ’ alla citta ’ di ’New York ’ ?

select distinct ar.comp, l1.citta, l2.citta
from arrpart as ar, luogoAeroporto as l1, luogoAeroporto as l2
where l1.citta = 'Roma'
	and l2.citta = 'New York'
	and l1.aeroporto = ar.partenza
	and l2.aeroporto = ar.arrivo
	
--8) Quali sono gli aeroporti (con codice IATA, nome e luogo) nei quali partono voli della compagnia di nome ‘MagicFly’ ?

select distinct ae.nome, ae.codice, la.citta
from aeroporto as ae, luogoaeroporto as la, arrpart
where arrpart.comp ='MagicFly'
	and arrpart.partenza=ae.codice
	and la.aeroporto = ae.codice
	
-- 9) Quali sono i voli che partono da un qualunque aeroporto della città di ‘Roma’  e atterrano ad un qualunque aeroporto della città di ‘New York’ ? Restituire: codice del volo, nome della compagnia, e aeroporti di partenza e arrivo.

select distinct ap.codice as codice_volo, ap.comp as compagnia, ap.partenza, ap.arrivo
from arrpart ap, luogoaeroporto la1, luogoaeroporto la2
where ap.arrivo = la1.aeroporto
	and ap.partenza = la2.aeroporto
	and la1.citta = 'New York'
	and la2.citta = 'Roma'
	
	
-- 10. Quali sono i possibili piani di volo con esattamente un cambio (utilizzando solo voli della stessa compagnia) da un qualunque aeroporto della città di ‘Roma’ ad un qualunque aeroporto della città di ‘New York’ ?  Restituire: nome della compagnia, codici dei voli, e aeroporti di partenza, scalo e arrivo.


select ap1.comp as compagnia, ap1.codice as codice_volo_1, ap1.partenza as partenza, ap1.arrivo as scalo, 
	ap2.codice as codice_volo_2, ap2.arrivo as arrivo
from arrpart ap1, arrpart ap2, luogoaeroporto la1, luogoaeroporto la2
where ap1.arrivo = ap2.partenza
	and ap1.comp = ap2.comp
	and la1.citta = 'Roma'
	and la2.citta = 'New York'
	and ap1.partenza = la1.aeroporto
	and ap2.arrivo = la2.aeroporto
	
	
-- 11. Quali sono le compagnie che hanno voli che partono dall’aeroporto ‘FCO’, atterrano all’aeroporto ‘JFK’, e di cui si conosce l’anno di fondazione

select distinct c.nome
from arrpart ap, compagnia c
where c.nome = ap.comp
	and ap.partenza = 'FCO'
	and ap.arrivo = 'JFK'
	and c.annoFondazione is not Null
