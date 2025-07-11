# Input students
all_students = set()
cricket = set()
football = set()

n = int(input("Total students: "))

for i in range(n):
    roll = int(input(f"\nRoll no {i+1}: "))
    all_students.add(roll)
    
    sport = input("Plays (C)ricket, (F)ootball, (B)oth, or (N)one? ").upper()
    
    if sport in ['C', 'B']:
        cricket.add(roll)
    if sport in ['F', 'B']:
        football.add(roll)

# Calculate results
both = cricket & football
one_sport = cricket ^ football  # XOR gives elements in only one set
neither = all_students - (cricket | football)

# Print results
print("\nBoth sports:", both)
print("Only one sport:", one_sport)
print("Neither sport:", neither)