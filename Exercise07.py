def isFizzBuzz(a):
    if (a%5==0 and a%3==0):
        print("FizzBuzz")
    elif a%5==0:
        print("Buzz")
    elif a%3==0:
        print("Fizz")
    else:
        print("Not a Fizz-buzz number")
    
    
a = input("Enter a number: ")
a = int(a)
isFizzBuzz(a)