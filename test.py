db={"a":"11","b":"22","c":"33"}
for i in range(5):
    username=input("Enter your username: ")
    password=input("Enter your password: ")
    if (db[username]==password):
        print("Welcome to ABC system")
        break
    else:
        continue
else:
    print("No longer Authorised")

