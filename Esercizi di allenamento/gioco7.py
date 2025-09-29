def merge_overwrite(a: dict, b: dict) -> dict:
    c = a.copy()
    for key,values in b.items():
        c[key]=values
        
    return c
    
    
        
    
    
    
    
    
    
a = {"terra": "antica", "fuoco": "debole", "acqua": "limpida"}
b = {"fuoco": "ardente", "aria": "libera"}

print(merge_overwrite(a,b))