def solution(n, infection, edges, k):
    answer = 0
    dp = [[1] * 3 for _ in range(k+1)]
    infectmapprev = [[infection] * 3]
    infectmapnext = [[infection] * 3]
    for i in range(1, k+1):
        for j in range(3):
            dp[i][j], infectmapnext = getDp(edges, infectmapprev, j)
        for j in range(3):
            infectmapprev[j] = infectmapnext[j]
	
    

def getDp(edges, infectmapprev, pipeNum):
    """
	pipeNum 파이프를 열 때의 최대 지도를 구해줌
    두 가지 경우 비교해서 알아서 최대 지도를 구해줌
    반환: 최대 숫자, 지도
    """
    map1, map2, map3 = 1, 1, 1
	
	
	return