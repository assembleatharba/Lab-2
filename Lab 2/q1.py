how_many=int(input("How many numbers do you wish to store in the list?"))
num=[]
i=0
while i<how_many:
    number=int(input("Enter number"))
    num.append(number)
    i+=1
print(num)

#using built in functions:
print(f"The maximum number in the list is {max(num)} and the minimum number is {min(num)}")
print(f"The list in ascending order is: {sorted(num)}")
print(f"The list with duplicate items removed is: {list(set(num))}")

#without using built in functions:
maximum=num[0]
minimum=num[0]
for j in num:
    if maximum<j:
        maximum=j
for j in num:
    if minimum>j:
        minimum=j
print(f"The maximum number is {maximum} and the minimum number is {minimum}")
new_num=[]
minimum=num[0]
z=0

print(f"The list in ascending order is {new_num}")

