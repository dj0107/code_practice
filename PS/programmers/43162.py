from collections import deque
def solution(n, computers):
    answer = 0
    visited = [False] * n
    q = deque()
    
    for i in range(n):
        if visited[i]: continue
        answer += 1
        q.append(i)
        visited[i] = True
        while q:
            point = q.popleft()
            for j in range(n):
                if computers[point][j] and not visited[j]:
                    q.append(j)
                    visited[j] = True
        
            

    return answer

