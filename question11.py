numbers = [10, 30, 30, 69, 69, 77777, 87878787, 77777, 10]
unique_set = set(numbers)
list2 = []
for i in unique_set:
    list2.append(i)
list2.sort()
print("The sorted list is: ")
print(list2)