import itertools

def available_row_col(row,col,n):
    if row<0 or row>=n:
        return False
    if col<0 or col>=n:
        return False
    return True


def movement(direction, row, col):
    movement = {'sw':(1,0),'e':(0,1),'nw':(-1,-1)}
    row+=movement[direction][0]
    col+=movement[direction][1]
    return row, col
    

def solution(n):   
    array = [[-1]*i for i in range(1,n+1)]  # [[-1],[-1,-1],[-1,-1,-1], ...]
    direction = {'sw':'e','e':'nw','nw':'sw'}
    current_direction = 'sw'
    row,col=0,0
    total_cnt = int(n*(n+1)/2)
    visited= 1
    
    for i in range(1,total_cnt+1):
        array[row][col] = visited
        next_row,next_col = movement(current_direction,row,col)
        if available_row_col(next_row,next_col,n)==False or array[next_row][next_col]!=-1:
            current_direction = direction[current_direction]
            next_row,next_col = movement(current_direction, row, col)
        row, col = next_row, next_col
        visited+=1
    # 일련의 방향성을 가지고 있는 배열을 만들고 싶을때 사용할 수 있는 개념
    # 이전 방향 유지가 우선순위, 해당 셀이 없을 경우 다음 방향으로 진행하는 방식
    
    answer = list(itertools.chain(*array))
    return answer