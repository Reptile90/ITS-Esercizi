import React, { useState } from 'react';
import { Card, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { ScrollArea } from "@/components/ui/scroll-area";

export default function LibraryApp() {
    const [catalogo, setCatalogo] = useState([]);
    const [titolo, setTitolo] = useState("");
    const [autore, setAutore] = useState("");
    const [messaggio, setMessaggio] = useState("");

    const aggiungiLibro = () => {
    if (!titolo || !autore) {
        setMessaggio("Inserisci titolo e autore.");
        return;
    }
    const nuovoLibro = { titolo, autore, disponibile: true };
    setCatalogo([...catalogo, nuovoLibro]);
    setMessaggio(`Libro '${titolo}' aggiunto.`);
    setTitolo("");
    setAutore("");
    };

    const prestaLibro = (titolo) => {
    const nuovoCatalogo = catalogo.map(libro => {
        if (libro.titolo === titolo && libro.disponibile) {
        setMessaggio(`Il libro '${titolo}' è stato prestato.`);
        return { ...libro, disponibile: false };
        }
        return libro;
    });
    setCatalogo(nuovoCatalogo);
    };

    const restituisciLibro = (titolo) => {
    const nuovoCatalogo = catalogo.map(libro => {
        if (libro.titolo === titolo && !libro.disponibile) {
        setMessaggio(`Il libro '${titolo}' è stato restituito.`);
        return { ...libro, disponibile: true };
        }
        return libro;
    });
    setCatalogo(nuovoCatalogo);
    };

    return (
    <div className="p-6 max-w-4xl mx-auto">
        <h1 className="text-3xl font-bold mb-4">Biblioteca Virtuale</h1>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mb-6">
        <Input
            placeholder="Titolo del libro"
            value={titolo}
            onChange={(e) => setTitolo(e.target.value)}
        />
        <Input
            placeholder="Autore"
            value={autore}
            onChange={(e) => setAutore(e.target.value)}
        />
        <Button onClick={aggiungiLibro} className="col-span-1 md:col-span-2">
            Aggiungi Libro
        </Button>
        </div>

        {messaggio && <p className="text-green-600 mb-4">{messaggio}</p>}

        <ScrollArea className="h-96">
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            {catalogo.map((libro, index) => (
            <Card key={index} className="shadow-md">
                <CardContent className="p-4">
                <h2 className="text-xl font-semibold">{libro.titolo}</h2>
                <p className="text-gray-700">Autore: {libro.autore}</p>
                <p className={`text-sm ${libro.disponibile ? 'text-green-600' : 'text-red-600'}`}>
                    {libro.disponibile ? "Disponibile" : "In prestito"}
                </p>
                <div className="mt-2 flex gap-2">
                    <Button onClick={() => prestaLibro(libro.titolo)} disabled={!libro.disponibile}>
                    Presta
                    </Button>
                    <Button onClick={() => restituisciLibro(libro.titolo)} disabled={libro.disponibile}>
                    Restituisci
                    </Button>
                </div>
                </CardContent>
            </Card>
            ))}
        </div>
        </ScrollArea>
    </div>
    );
}
