import sys
input = sys.stdin.readline

# 입력
n, m = map(int, input().split())  # n: 심사대 수, m: 사람 수
times = [int(input()) for _ in range(n)]

# 이분 탐색으로 최소 시간 구하기
start = 1
end = max(times) * m  # 최악의 경우
res = end

while start <= end:
    mid = (start + end) // 2
    cnt = sum(mid // t for t in times)  # mid분 동안 심사 가능한 사람 수

    if cnt < m:  # 더 시간이 필요
        start = mid + 1
    else:        # 시간 충분, 최소 시간 후보
        res = mid
        end = mid - 1

print(res)