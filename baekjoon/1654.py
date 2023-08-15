# K, N = map(int, input().split())
# num_list = []
# for _ in range(K):
#     num_list.append(int(input()))

# for x in range(sum(num_list) // N + 2, 0, -1):
#     temp_sum = 0
#     for i in num_list:
#         temp_sum += i // x
#     if temp_sum == N:
#         print(x)
#         break