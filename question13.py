a = input("Enter a sentence: ")
a = a.strip().lower()
count = {}

for ch in a:
    if ch.isalpha():  # Only count alphabetic characters
        if ch in count:
            count[ch] += 1
        else:
            count[ch] = 1

print("Character frequencies:")
print(count)