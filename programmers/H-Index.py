def solution(citations):
    citations.sort(reverse=True)
    for h in range(citations[0], 0, -1):
        cnt = 0
        for i in citations:
            if h <= i:
                cnt += 1
        if cnt >= h and len(citations)-cnt<=h:
            return h
    # [0]
    return 0