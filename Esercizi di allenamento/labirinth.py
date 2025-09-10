def trova_percorso(maze:list[list[int]])->bool:
    start = None
    
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == "S":
                start = (i,j)
                break
            
    if start == None:
        return False
            
    def esplora(x,y,visitate):
        if x < 0 or x >= len(maze) or y < 0 or y >= len(maze[0]):
            return False
        
        if maze[x][y]=="1" or (x,y) in visitate:
            return False
        
        if maze[x][y] == "E":
            return True
        
        
        visitate.add((x,y))
        return(
            esplora(x + 1, y, visitate)or
            esplora(x - 1, y, visitate)or
            esplora(x, y + 1, visitate)or
            esplora(x, y - 1, visitate)
            )          
    return esplora(start[0], start[1], set())
    
    
    
    
    
    
    
    
    
    
maze4 = [
    ['S', '1', '1', '1'],
    ['1', '1', '1', '1'],
    ['1', '1', '1', '1'],
    ['1', '1', '1', 'E']
]


print(trova_percorso(maze4))