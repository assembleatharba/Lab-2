items = []
count = int(input("How many items would you like to add initially? "))
for i in range(count):
    item = input(f"Enter item {i+1}: ")
    items.append(item)
print("\nCurrent collection:", items)

while True:
    print("\nAvailable operations:")
    print("1. Add to stack (Push)")
    print("2. Remove from stack (Pop)")
    print("3. Add to queue (Enqueue)")
    print("4. Remove from queue (Dequeue)")
    print("5. Quit program")
    
    action = input("\nSelect operation (1-5): ")
    
    if action == '1':  # Push
        new_item = input("Enter item to add to top of stack: ")
        items.append(new_item)
        print(f"\nAdded '{new_item}' to stack")
        print("Updated stack:", items)
   
    elif action == '2':  # Pop
        if items:
            removed = items.pop()
            print(f"\nRemoved '{removed}' from stack")
            print("Updated stack:", items)
        else:
            print("\nStack is empty - nothing to remove")
            
    elif action == '3':  # Enqueue
        new_item = input("Enter item to add to end of queue: ")
        items.append(new_item)
        print(f"\nAdded '{new_item}' to queue")
        print("Updated queue:", items)
        
    elif action == '4':  # Dequeue
        if items:
            removed = items.pop(0)
            print(f"\nRemoved '{removed}' from front of queue")
            print("Updated queue:", items)
        else:
            print("\nQueue is empty - nothing to remove")
            
    elif action == '5':  # Exit
        print("\nClosing the program...")
        break
        
    else:
        print("\nInvalid selection - please choose 1-5")