list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = []
for i in range(len(list)):
    if i % 2 == 0:
        result.append(list[i])
    elif i > 1:
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            result.append(list[i])
print(result)