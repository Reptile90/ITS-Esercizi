//esercizio 1

let numero = 5

console.log(numero)

//esercizio 2
const PI = 3.14
console.log(PI)

//esercizio 3

let nome = "Marco"
console.log(nome)
nome = "Luca"
console.log(nome)

//esercizio 4

let saluto = "Ciao come stai?"
console.log(saluto)

//esercizio 5

let vero = true
console.log(vero)

//esercizio 6
let numeri = [1,2,3,4,5]
console.log(numeri)

//esercizio 7
let persona = {
    nome:"Mario Rossi",
    età:"30"
}
console.log(persona)

//esercizio 8
nome = "Stefano"
console.log(nome)

//esercizio 9
let eta ="35"
console.log(eta)

//esercizio 10

let verificato = true
console.log(verificato)

//esercizio 11
let num = [2,4,1,5,6,7,4,4,6,6,3]
console.log(num)

//esercizio 12
persona = {
    nome:"Stefano",
    cognome: "Reali",
    età: "35"
}
console.log(persona)

//esercizio 13

let nullo = null
console.log(null)

//esercizio 14

let nonDefinito
console.log(nonDefinito)

//esercizio 15

let divisione = "Stefano"/ 2
console.log(divisione)

//esercizio 16

let simbolo = Symbol
console.log(simbolo)

//esercizio 17

let num1 = 134
let num2 = 1409023
let somma = num1+num2
console.log(somma)

//esercizio 18

let sottrazione = num2 - num1
console.log(sottrazione)

//esercizio 19

let moltiplicazione = num2 * num1
console.log(moltiplicazione)

//esercizio 20

divisione = num2 / num1
console.log(divisione)

//esercizio 21
let resto = num2 % num1
console.log(resto)

//esercizio 22

num1 = num1 + 1
console.log(num1)

//esercizio 23

num1 = (num1 -1)
console.log(num1)

//esercizio 24
let pot = num1**2
console.log(pot)

//esercizio 25

let rq = Math.sqrt(num1)
console.log(rq)

//esercizio 26
let round = Math.round(divisione)
console.log(round)

//esercizio 27
const minimo = 1
const massimo = 10
const numeroCasuale = Math.floor(Math.random() * (massimo - minimo + 1)) + minimo
console.log(numeroCasuale)

//esercizio 28

const convNum = "340"
conversione = parseInt(convNum)

//esercizio 29

const stringa = "Ciao sono stefano"
console.log(stringa.length)

//esercizio 30

const stringa1 = "Ciao sono "
const stringa2 = "Stefano"
console.log(stringa1 +  stringa2)

//esercizio 31
const stringa3 = "Stefgano"
const stringa4 = "Stefano"
console.log(stringa3 === stringa4)
console.log(stringa4 === stringa2)

//esercizio 32
const stringNum = "340293402934029340"
console.log(parseInt(stringNum))

//esercizio 33
let stringa6 = "Ciao sono Stefano"
console.log(stringa6.includes(stringa2))

//esercizio 34

let stringa7 = "Supercalifragili"
console.log(stringa7.slice(0,5))


//esercizio 35

console.log(stringa2.toUpperCase())

//esercizio 36

const stringa8 = stringa2.toUpperCase()
console.log(stringa2.toLowerCase())

//esercizio 37

const nstring1 = "Ciao sono Stefano"
const nstring2 ="Stefano"
nuova ="Lorenzo"
console.log(nstring1.replace(nstring2,nuova))

//esercizio 38
const spazi = " Ciao sono stefano "
console.log(spazi.trim())

//esercizio 39
nome ="Lorenzo";
console.log(`Ciao, mi chiamo ${nome}.`);

//esercizio 40
console.log(`La somma dei numeri è ${somma}`)

//esercizio 41
console.log(`
    Nome: ${persona.nome}
    Cognome: ${persona.cognome}
    Età: ${persona.età}`
)

//esercizio 42
ind = "redhotchilipeppers"
console.log(`www.${ind}.com`)

//esercizio 43
ogg=["Mela","Arancia","Susina","Banana"]
html = "<ul>";
for(let oggetto of ogg){
    html += `<li>${oggetto}</li>`
}
html +="</ul>"
console.log(html)

//esercizio 44
const nome1 = "Marcel"
const messaggio = `Ciao ${nome1} spero che ti trovi bene all'ITS
Saluti ${nome}`
console.log(messaggio)

//esercizio 45
console.log(`Hai guadagnato € ${somma}`)


//esercizio 47
dataoggi = new Date()
console.log(dataoggi)

//esercizio 48
const data = new Date()
giorno = data.getDay()
console.log(giorno)

//esercizio 49
const mese = data.getMonth()
console.log(mese)

//esercizio 49
const anno = data.getFullYear()
console.log(anno)

//esercizio 50
const datanascita = 1990
