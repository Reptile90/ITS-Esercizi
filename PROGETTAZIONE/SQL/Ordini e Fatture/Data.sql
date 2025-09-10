BEGIN;

-- Nazioni
INSERT INTO Nazione (nome) VALUES
  ('Italia'), ('Francia'), ('Germania');

-- Regioni
INSERT INTO Regione (nome, nazione) VALUES
  ('Lazio', 'Italia'), ('Île-de-France', 'Francia'), ('Baviera', 'Germania');

-- Città
INSERT INTO Citta (nome, regione, nazione) VALUES
  ('Roma', 'Lazio', 'Italia'),
  ('Parigi', 'Île-de-France', 'Francia'),
  ('Monaco', 'Baviera', 'Germania');

-- Direttori
INSERT INTO Direttore (nome, cognome, cf, data_nascita, anni_servizio, citta, regione, nazione) VALUES
  ('Giulia', 'Rossi', 'RSSGLI85A01H501U', '1985-01-01', 10, 'Roma', 'Lazio', 'Italia'),
  ('Pierre', 'Dubois', 'DBSPRR75B22F205Z', '1975-02-22', 20, 'Parigi', 'Île-de-France', 'Francia'),
  ('Hans', 'Müller', 'MLRHNS70C15D305Y', '1970-03-15', 25, 'Monaco', 'Baviera', 'Germania');

-- Dipartimenti
INSERT INTO Dipartimento (nome, indirizzo, direttore) VALUES
  ('Amministrazione', ROW('Via Nazionale', '12', '00184'), 'RSSGLI85A01H501U'),
  ('Marketing', ROW('Rue Lafayette', '88', '75009'), 'DBSPRR75B22F205Z'),
  ('Produzione', ROW('Hauptstrasse', '5', '80331'), 'MLRHNS70C15D305Y');

-- Fornitori
INSERT INTO Fornitore (ragione_sociale, partitaiva, indirizzo, telefono, email) VALUES
  ('TechItalia Srl', '12345678901', ROW('Via Roma', '45', '00100'), '+393331234567', 'info@techitalia.it'),
  ('FranceLog SA', '23456789012', ROW('Boulevard Haussmann', '22', '75008'), '+33123456789', 'contact@francelog.fr'),
  ('BayernTools GmbH', '34567890123', ROW('Königstrasse', '10', '80335'), '+491511234567', 'sales@bayerntools.de');




-- Ordini
INSERT INTO Ordine (id, data_stipula, imponibile, aliquotaiva, descrizione, stato, fornitore, dipartimento) VALUES
  (1, '2025-01-10', 1200.00, 0.22, 'Computer portatili', 'inviato', '12345678901', 'Amministrazione'),
  (2, '2025-02-15', 800.00, 0.20, 'Materiale promozionale', 'in preparazione', '23456789012', 'Marketing'),
  (3, '2025-03-20', 1500.00, 0.19, 'Attrezzature industriali', 'da saldare', '34567890123', 'Produzione');

COMMIT;





