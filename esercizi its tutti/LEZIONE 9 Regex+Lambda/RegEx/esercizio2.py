import re

def extract_emails(text) -> list:
    return re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)

text = "Contattaci a info@azienda.com oppure support@help.org"
print(extract_emails(text))  # ['info@azienda.com', 'support@help.org']