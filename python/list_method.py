# 특정 값 가지는 원소 모두 제거
arr = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5}

result = [i for i in arr if i not in remove_set]
print(result)

# sorted() with key
arr = [('aaa', 35), ('bbb', 75), ('ccc', 68)]
result = sorted(arr, key=lambda x: x[1], reverse=True)
print(result)