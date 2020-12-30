def solution(number, k):
    num_array = list(number)
    max_idx = num_array[:k].index(max(num_array[:k]))
    remain = k-max_idx-1
    # result = int(num_array[max_idx])*(10**(len(num_array)-k-1))
    remains = num_array[max_idx+1:]
    while True:
        remains.remove(min(remains))
        remain-=1
        if remain ==-1:
            break
    remains.insert(0,num_array[max_idx])
    result = ''.join(remains)
    print(remains)
    return result
    
        
        
    
    
    
    
    
    
    
