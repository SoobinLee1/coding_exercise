def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        skill_in_tree = [skill_tree.find(s) for s in skill]    # skill_tree에서 해당 문자 s의 index를 반환
        for idx, element in enumerate(skill_in_tree[1:]):
            if element==-1:   # 해당 문자가 없을 때 (-1)
                continue
            if skill_in_tree[idx]==-1 or skill_in_tree[idx]>element:
                # 앞 문자가 없거나 그 다음 element보다 클 때 (즉, 앞에있어야할 게 뒤에 있을 때)
                break
        else:
            answer+=1
    return answer