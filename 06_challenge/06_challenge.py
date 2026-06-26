import conf

def fizzbuzz(max_num):
    "This method implements FizzBuzz"
    
    three_mul = 'fizz'
    five_mul = 'buzz'
    num1 = conf.num1
    num2 = conf.num2

    for i in range(1, max_num):
        if i % num1 == 0 and i % num2 == 0:
            print(i, three_mul + five_mul)
        elif i % num1 == 0:
            print(i, three_mul)
        elif i % num2 == 0:
            print(i, five_mul)

if __name__ == '__main__':
    fizzbuzz(100)