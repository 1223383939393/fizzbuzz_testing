class FizzBuzz:

    def __init__(self):
        "Initializer"
        self.num1 = 3
        self.num2 = 5
        self.three_mul = 'fizz'
        self.five_mul = 'buzz'

    def fizzbuzz(self, max_num):
        "This method implements FizzBuzz"

        for i in range(1, max_num):
            if i % self.num1 == 0 and i % self.num2 == 0:
                print(i, self.three_mul + self.five_mul)
            elif i % self.num1 == 0:
                print(i, self.three_mul)
            elif i % self.num2 == 0:
                print(i, self.five_mul)

if __name__ == '__main__':
    test_obj = FizzBuzz()
    test_obj.fizzbuzz(100)