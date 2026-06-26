def fizzbuzz(max_num):
    "This method implements FizzBuzz"
    for i in range(1, max_num):
        if i % 3 == 0 and i % 5 == 0:
            print(i, "fizzbuzz")
        elif i % 3 == 0:
            print(i, "fizz")
        elif i % 5 == 0:
            print(i, "buzz")

#----START OF SCRIPT
if __name__ == '__main__':
    fizzbuzz(100)