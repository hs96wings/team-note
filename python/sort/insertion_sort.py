# 시간 복잡도 O(N^2), 최선의 경우 O(N)

arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(arr)):
    for j in range(i, 0, -1):
        if arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
        else: # 자기보다 작으면 멈춤
            break

print(arr)