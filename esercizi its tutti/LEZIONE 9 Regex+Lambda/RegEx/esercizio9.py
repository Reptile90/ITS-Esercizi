import re

def find_fc(text):
    return re.findall(r"\b(?:CF:? )?([A-Z]{6}\d{2}[A-Z]\d{2}[A-Z]\d{3}[A-Z])\b", text)

testo = "Mario Rossi CF: RSSMRA85M01H501Z, mentre Maria Bianchi ha il CF BNCMRA85T41H501Y."
codici = find_fc(testo)
print(codici)