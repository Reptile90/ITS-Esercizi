def contains_line(lines: list[str], needle: str) -> bool:
    filename = 'textio_contains.txt'
    with open(filename,"w",encoding="utf-8") as f:
        f.write(lines+ "\n")
        
    with open(filename, "r", encoding="utf-8") as f:
            lines = f.readlines()
        
    for line in lines:
        clean = line.strip()
        if clean == needle:
            return True
            
        return False
            
        