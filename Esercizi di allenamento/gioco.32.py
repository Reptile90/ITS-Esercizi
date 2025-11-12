def count_lines(lines: list[str]) -> int:
    filename = 'textio_count.txt'
    with open(filename,"w", encoding="utf-8") as file:
        file.write("\n".join(lines))
        
        
    with open(filename,"r") as f:
        lines = f.readlines()
    
    count = 0
    for line in lines:
        count += 1
        
    return count
        