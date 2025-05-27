from typing import Self
from datetime import datetime.date

class RealGEZ(float):
def __new__(cls, v:int|float)->Self
	if v < 0:
		raise ValueError(f"Value v {v} must be >= 0")
	return float.__new__(cls, v)
	
	
	
class RealGZ(RealGEZ)
	def__new__(cls, v:int|float|str)->Self:
	if v <= 0:
		raise ValueError(f"Value v {v} must be >0")
		
	return RealGEZ.__new__(cls,v)
	
	
	
class Impiegato:
	_nome:str
	_cognome:str
	_stipendio_annuale_eur:RealGZ
	_data_affarenza:datetime.date
	_nascita:datetime.date #<<immutable>>
	_dipartimento:Dipartimento|None
	
	def nome(self)->str
		return self._nome
	def nome(self)->str:
		return self._cognome
	def stipendio_annuale(self)-RealGZ:
		return self._stipendio_annuale_eur:
	def data_afferenza(self)->datetime.date:
		return self._data_afferenza
	def nascita(self)->datetime.date
		return self._nascita
		
	def dipartimento(self)->Dipartimento|None
		return self.dipartimento
		
#se non è immutabile e non noto alla nascita posso usare i setter
#se è immutabile e noto alla nascita solo getter

	def set_nome(self, v:str)->None
		self._nome:str = v
	def set_cognome(self,v:str)->None
		self._cognome:str = v
	def set_stipendio_annuale_eur(self,v:RealGZ)-None
		self._stipendio_annuale_eur = v
	def set_data_afferenza(self, v:datetime.date)->None
		self._data_afferenza(self, v:datetime.date)->None
	#def set_nascita(self, v:... ) <----- NO perchè è immutabile
	
	def set_dipartimento(self, v:Dipartimento|None)->None
		self._dipartimento = v
		
		
	def unset_dipartimento(self)->None
		self._dipartimetno = None   #cancella il dipartimento solo se il vincolo di molteplicità è 0..1 altrimenti rimane DIpartimento
		
		
	#to do: incompleto! Manca l'inserimento del link "afferenza
	def __init__(self,*, nome:str, cognome:str, stipendio_annuale_eur:RealGZ, data_afferenza:datetime.date, nascita:datetime.date, dipartimento:Dipartimento)
	
	self.set_nome(nome)
	self.set_cognome(cognome)
	self.set_stipendio_annuale_eur(stipendio_annuale_eur)
	self.set_data_afferenza(data_afferenza)
	self.nascita = nascita
	self.set_dipartimento(dipartimento)
	
''nel caso ci fosse un associazione di classe Afferenza''

class _afferenza:
	_impiegato:IMpiegato #<<immutable>>
	_dipartimento:Dipartimento #>>Immutable>>
	_data_afferenza:datetime.date
	
	
	def impiegato(self)->Impiegato:
		return self._impiegato
	def dipartimento(self)->Dipartimento
		return self._dipartimento
	def data_afferenza(self)-> datetime.date
		return self._data_afferenza
		
	def __init__(self, impiegato:Impiegato, dipartimento:Dipartimento, data_affarenza:datetime.date)
	
	def __hash__(self)->int:
		return hash((self.impiegato(), self.dipartimento()))
		
	def __eq__(self,other:any)->bool
		if not isnstance(other,afferenza):
		 	return False
		 else:
		 	return self.impiegato() == other.impiegato() and self.dipartimento () == other.dipartimento()	
	
#esempio:
#i1= IMpiegato("Mario", ...)
#i2 = Impiegato"Anna", ...)
#d1= Dipartimento("Informatica")

#i1.set_afferenza(d1, "2025-12-01")

#l'utente non può creare un link , l'utente deve dare gli input

#es: self.set_afferenza(self,dipartimento, data_afferenza)

#d2= DIpartimento("FIsica"")

#i2.set_afferenza("Anna", "2025-12-01") 
#facciamo cosi in modo di far creare direttamente all'oggetto il link afferenza facendo un set afferenza con input il dipartimento e la data

l = afferenza(i1,d1) #da impedire la creazione diretta del link

l2 = affarenza(i1,d1) #da impedire la creazione diretta dei link duplicati




	
	
	
	
	
