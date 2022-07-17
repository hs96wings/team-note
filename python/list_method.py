# 특정 값 가지는 원소 모두 제거
arr = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5}

result = [i for i in arr if i not in remove_set]
print(result)