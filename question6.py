# Get numbers from user
nums = ()
n = int(input("Enter how many numbers: "))
for _ in range(n):
    num = int(input("Enter a number: "))
    nums += (num,)

# Calculate and show results
print("Numbers:", nums)
print("Average:", sum(nums)/n)

sorted_nums = sorted(nums)
mid = n//2
median = (sorted_nums[mid-1] + sorted_nums[mid])/2 if n%2 == 0 else sorted_nums[mid]
print("Median:", median)

counts = {}
for num in nums:
    counts[num] = counts.get(num, 0) + 1
    
max_count = max(counts.values())
mode = [num for num, cnt in counts.items() if cnt == max_count]
print("Mode:", mode)