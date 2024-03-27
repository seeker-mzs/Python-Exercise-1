a = 6
b = input("Enter a number: ")
b = int(b)
while(1):
    if b<a:
        print("your guess is almost there")
        b = input("Try again: ")
        b = int(b)
    elif b>a:
        print("your guess is higher")
        b = input("Try again: ")
        b = int(b)
    else:
        print("Your Guess Is Correct")
        break
    