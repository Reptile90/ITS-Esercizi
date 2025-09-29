def invert_unique(d: dict) -> dict:
    a = {}
    for key,values in d.items():
        a[values]=key
    return a
    
    
    
    
    
    
    
d = {
    "sole": "oro",
    "luna": "argento",
    "mare": "blu",
    "foresta": "verde"
}
print(invert_unique(d))