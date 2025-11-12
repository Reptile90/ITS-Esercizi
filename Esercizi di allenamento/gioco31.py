def write_and_read(lines: list[str]) -> list[str]:
    filename = 'textio_write_and_read.txt'
    
    with open(filename,"w", encoding="utf-8") as file:
        for line in lines:
            file.write(line + "/n")
            
            
    result = []
    with open(filename,"r",encoding="utf-8"):
        for line in lines:
            result.append(line.strip())
            
            
    return result
        