sentence = input("Enter a sentence with space: ")
vowels = "aeiouAEIOU"
used_vowels = set()
for char in sentence:
    if char in vowels:
        used_vowels.add(char.lower())  
print("Unique vowels used:", used_vowels)
