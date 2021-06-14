print("--------------------------------CONTACT BOOK-------------------------------")
print("0.QUIT")
print("1. Add the contact number in the contact book")
d1 = {}
while True:
    n = int(input("Enter Number[0/1/2] :- "))
    # name = input("enter name :- ")
    if n == 1:
        name = input("Enter Name :- ")
        phno = int(input("Enter your contact number :- "))
        d1[name] = phno
    elif n == 2:
        name1 = input("Enter name to search the contact number in contact book ")
        print("contact number of",name1,"is",d1[name1])
    elif n == 3:
        break