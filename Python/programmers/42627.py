import heapq
def solution(jobs):
    n = len(jobs)
    answer = 0
    #jobs: [x,y]: x초에 yms 걸리는 작업이 들어옴.
    schedule = [[]] * 1001 # idx 초에 (소요시간, 번호) 인 리스트

    priority = []
    for i in range(n):
        schedule[jobs[i][0]].append((jobs[i][1], i))
        # prio = jobs[i][1] * 1000000 + jobs[i][0] * 1000 + i # 시간->시점->번호순 보장
        # heapq.heappush(priority, prio)
    finished = -1
    time = 0
    finishtime = []
    endtime = 0 # 작업 끝나는 시간
    while finished < n:
        for job in schedule[time]: # 작업 들어옴
            prio = job[0] * 10000000 + time * 1000 + job[1]
            heapq.heappush(priority, prio)
        if time >= endtime: #새 작업 할당
            finishtime.append(time)
            if not priority: break
            new = heapq.heappop(priority)
            endtime = time + new // 10000000 # 종료시간 계산
            finished += 1
            
        time += 1
    del finishtime[0]
    answer = sum(finishtime) // n
    print(finishtime)
    return answer