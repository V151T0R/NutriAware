t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    
    pop_count = 0
    pos = 0
    
    while n > 0:
        cost = 2 ** pos
        can_set= min(k, n // cost)    
                 
        pop_count += can_set
        n -= can_set *cost
        pos += 1
        
        if can_set == 0:  break
        
    print(pop_count)