def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        skill_in_tree = [skill_tree.find(s) for s in skill]    # skill_tree에서 해당 문자 s의 index를 반환
        for idx, element in enumerate(skill_in_tree[1:]):
            if element==-1:   
                # 해당 문자가 없을 때 (-1) 마지막 문자에 대해서는 없어도 그만이기 때문에 일단 여기서는 -1이 떠도 continue 처리하고, 다음 if 문에서 skill의 문자가 없을 경우 break 처리
                continue
            if skill_in_tree[idx]==-1 or skill_in_tree[idx]>element:
                # 앞 문자가 없거나 그 다음 element보다 클 때 (즉, 앞에있어야할 게 뒤에 있을 때)
                break
        else:   # for~ else~ 구문 : 앞선 for문이 break 없이 다 수행될 경우 else가 실행됨. 별도의 flag가 필요 없어지는 코드
            answer+=1
    return answer
