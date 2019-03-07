#Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten, a prime number is a number that has no divisors.). You can (and should!) use your answer to Exercise 4 to help you. Take this opportunity to practice using functions,
def get_num():
    return int(input("Enter your number to check prime or not"))

def check_prime(x):
    for i in range(2,x/2+1):
        if x%i==0:
            return 0
    return 1

x=get_num()
y=check_prime(x)
if y:
    print("{} is a prime number".format(x))
else:
    print("{} is not a prime number".format(x))


