username = input("Enter your username: ")

if len(username) >= 8:
    print("the username is strong")

elif len(username) >= 5:
    print("the username is medium")

else:
    print("the username is weak")

