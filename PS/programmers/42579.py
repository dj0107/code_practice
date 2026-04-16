from collections import Counter
def solution(genres, plays):
    answer = []
    genrearr = {}
    n = len(plays)
    cnt = Counter()
    for i in range(n):
        cnt[genres[i]] += plays[i]
        if genres[i] in genrearr:
            genrearr[genres[i]].append((i, plays[i]))
        else:
            genrearr[genres[i]] = [(i, plays[i])]
    
    comm = cnt.most_common()
    for values in genrearr.values():
        values.sort(key=lambda x: x[1] ,reverse = True)

    for genre in comm:
        answer.append(genrearr[genre[0]][0][0])
        if len(genrearr[genre[0]]) > 1:
            answer.append(genrearr[genre[0]][1][0])

    return answer