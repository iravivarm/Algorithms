n=15

def fizzBuzz(n):
    # Write your code here
    for i in range(1, n+1):
        # print(i)
        if i % 3 == 0 and i%5 ==0:
            print("FizzBuzz")
        elif i % 3 == 0 and i % 5 != 0:
            print("Fizz")
        elif i % 3 != 0 and i % 5 == 0:
            print("Buzz")
        elif i % 3 != 0 and i % 5 != 0:
            print(i)

print(fizzBuzz(n))