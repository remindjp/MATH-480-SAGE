def directions(id, method):
    up = id - 19
    down = id + 19  
    left = id - 1 
    right = id + 1 
                            
    if up >= 0: #up
        method(up)
                        
    if down <= 19 * 19 - 19: 
        method(down)

    if left >= 0 and left % 19 != 18: 
        method(left) 
                                                                
    if right < 19 * 19 and right % 19 != 0:                
        method(right)
        