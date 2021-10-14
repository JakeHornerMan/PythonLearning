def fizzBuzz():
    for num in range(1,101):
        if num % 5 == 0 and num % 3 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 ==0:
            print("Buzz")
        else:
            print(num)

def fibonacci():
    a,b = 0,1
    for i in range(0,10):
        print(a)
        a,b = b, a + b

