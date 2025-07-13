import re

class Url(str):
    pattern = re.compile (r"^https?://[a-zA-Z0-9\-]+(\.[a-zA-Z0-9\-]+)+(/[a-zA-Z0-9\-_./]*)?$")
    
    def __init__(self, url):
        if not self.isValid(url):
            raise ValueError ("L'URL inserita non è valida")
        self.url = url
        
    @classmethod   
    def isValid(cls,url:str)->bool:
        return bool(cls.pattern.fullmatch(url))