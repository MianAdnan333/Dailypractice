m1 = int(input("Enter the marks:"))
m2 = int(input("Enter the marks:"))
m3 = int(input("Enter the marks:"))
m4 = int(input("Enter the marks:"))

total_percentage= (m1+m2+m3+m4)/400*(100)

if(total_percentage>=40 and (m1 >= 33 and m2 >= 33 and m3 >= 33 and m4 >= 33) ):
    print("congrats your passed",total_percentage)

else:
    print("your are failed",total_percentage)