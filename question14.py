dict1 = {}
print("Product Management System")
print("Select an option below:")

while True:
    print("\n1. Add new product to inventory")
    print("2. Modify existing product price")
    print("3. Search products by price range")
    try:
        choice = int(input("Your selection: "))
    except ValueError:
        print("Invalid input - please enter a number (1-3).")
        continue

    if choice == 1:
        product = input("Product name to add: ")
        try:
            price = int(input("Enter product price (numbers only): "))
        except ValueError:
            print("Price must be a numeric value.")
            continue
        dict1[product] = price
        print(f"'{product}' has been added to inventory.")
    elif choice == 2:
        a = input("Name of product to update: ")
        if a in dict1:
            try:
                b = int(input(f"New price for '{a}': "))
            except ValueError:
                print("Please enter a valid price amount.")
                continue
            dict1[a] = b
            print(f"Price for '{a}' has been modified.")
        else:
            print("Error: Product not found in records.")
    elif choice == 3:
        try:
            a = int(input("Minimum price limit: "))
            b = int(input("Maximum price limit: "))
        except ValueError:
            print("Both values must be numbers.")
            continue
        found = False
        for product, price in dict1.items():
            if a <= price <= b:
                print(f"Match found: {product} (${price})")
                found = True
        if not found:
            print("No inventory matches your price criteria.")
    else:
        print("Error: Invalid menu selection.")

    cont = input("\nReturn to main menu? (yes/no): ").strip().lower()
    if cont != "yes":
        print("Exiting system...")
        break