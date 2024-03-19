for _ in range(int(input())):
  N = int(input())
  mbti = list(map(str, input().split()))
  ans = 8

  if N > 32 :
    print(0)
  else :
    for i in range(0, N-2):
      for j in range(i+1, N-1):
        for k in range(j+1, N):
          tmp = 0
          for l in range(4):
            if mbti[i][l] != mbti[j][l]: tmp += 1
            if mbti[i][l] != mbti[k][l]: tmp += 1
            if mbti[j][l] != mbti[k][l]: tmp += 1
          ans = min(tmp, ans)
    print(ans)


    # for i in range(N):
    #   for j in range(N):
    #     for k in range(N):
    #       tmp = 0
    #       if i == j or j == k or i == k:
    #         continue

    # 0 1 2
    # 1~