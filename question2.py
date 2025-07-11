first_list = [1, 2, 3, 4, 5]
second_list = [4, 5, 6, 7, 8]
third_list = []
for i in first_list:
    if i not in second_list:
        third_list.append(i)
for i in second_list:
    if i not in first_list:
        third_list.append(i)
print(f"Merged List without common elements: {third_list}")