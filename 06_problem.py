p1 = "ohh man"
p2 = "your a greate man"
p3 = "but its a lie"

message = input("enter the message:")

if((p1 in message) or p2 in message or p3 in message):
    print("its a joke")

else:
    print(" i am serious")