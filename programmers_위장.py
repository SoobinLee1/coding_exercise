from collections import defaultdict

def solution(clothes):
    answer = 1
    clothes_dict = defaultdict(list)
    for c in clothes:
        clothes_dict[c[1]].append(c[0])
    
    for what_clothes in clothes_dict.keys():
        answer *= len(clothes_dict[what_clothes])+1
    return answer-1