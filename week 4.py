numbers = [0,1,1,2,5,6,8,2,4,6,8]
result = [i for i in set(numbers) if i % 2 == 0]
result.sort()
print(result)
