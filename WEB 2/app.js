import * as util from "./util.js"

console.log(util)

console.log("Funziona")

for(let i=0;i<4;i++){
    console.log(i)
}



const arr1 =[1,2,3]

arr1.push(4)

const arr2=arr1; 
console.log(arr1,arr2)


const prof={
    nome:"Stefano",
    cognome:"Reali",
    eta:34,
    indirizzo:{
        via:"viale spagna 17",
        citta:"pomezia"}
    
    
    }

console.log(prof.indirizzo,via);
console.log(prof["cognome"])

const prof2=new Object();


prof2.nome="stefano"
prof2.cognome ="reali"

console.log(prof2)


function persona(nome=", cognome="){
    this.nome=nome;
    this.cognome=this.cognome;
}
persona.prototype.CalcolaCodiceFiscale=function(){
    return"codice_fiscale prototype";
}

const robdel = new persona("robe,del");
const mariorossi=new persona("mario","rossi");

mariorossi.rossi.CalcolaCodiceFiscale()

