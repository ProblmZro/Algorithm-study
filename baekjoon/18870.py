import sys
input = sys.stdin.readline

# def QuickSort(arr):
#   if len(arr) <= 1: return arr

#   pivot = arr[0]
#   left = [x for x in arr[1:] if x<=pivot]
#   right = [x for x in arr[1:] if x>pivot]

#   return QuickSort(left) + [pivot] + QuickSort(right)

N = int(input())
X1 = list(map(int, input().split()))
X2 = sorted(list(set(X1)))

dic = {X2[i] : i for i in range(len(X2))}

for i in X1:
    print(dic[i], end=" ")