def solution(priorities, location):
    ordered_prior = list(zip(priorities, list(range(len(priorities)))))
    res = []
    length = len(priorities)
    print(ordered_prior)
    
    while len(ordered_prior)>=1:
        item = ordered_prior[0]
        del ordered_prior[0]
        if item[0]==max(priorities):
            res.append(item)
            priorities.remove(item[0])
        else:
            ordered_prior.append(item)
    
    for i, item in enumerate(res):
        if item[1]==location:
            return i+1
    