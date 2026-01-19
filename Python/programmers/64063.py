import sys
sys.setrecursionlimit(100000)

def solution(k, room_number):
    parent = {}  

    def find(x):
        
        if x not in parent:      
            return x
        
        parent[x] = find(parent[x])
        return parent[x]

    answer = []
    for want in room_number:
        room = find(want)        
        answer.append(room)
        parent[room] = find(room + 1)
    return answer

rooms = [1, 10, 1, 10, 1, 10]
k = 10
print(solution(k, rooms))