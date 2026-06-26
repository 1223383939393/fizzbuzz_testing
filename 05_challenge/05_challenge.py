def fizzbuzz(max_num):
    "This method implements FizzBuzz"
    
    three_mul = 'fizz'
    five_mul = 'buzz'
    with open('mifile.txt', 'r') as f:
        print('i have created')
        num1 = int(f.readline())
        num2 = int(f.readline())
        max_num = int(f.readline())
         
    for i in range(1, max_num):
        if i % num1 == 0 and i % num2 == 0:
            print(i, three_mul + five_mul)
        elif i % num1 == 0:
            print(i, three_mul)
        elif i % num2 == 0:
            print(i, five_mul)
        else:
            print(i)

if __name__ == '__main__':
    fizzbuzz(100)