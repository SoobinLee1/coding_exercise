def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    max_cnt, min_cnt,total_cnt=0,0,len(people)
    weight = people[max_cnt]
    while max_cnt != total_cnt-min_cnt-1:
        if weight+people[total_cnt-min_cnt-1] > limit:
            answer+=1
            max_cnt+=1
            weight=people[max_cnt]
        elif weight+people[total_cnt-min_cnt-1]<=limit:
            weight+=people[total_cnt-min_cnt-1]
            min_cnt+=1
    return answer+1