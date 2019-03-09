#Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. Take this opportunity to think about how you can use functions. Make sure to ask the user to enter the number of numbers in the sequence to generate.(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the sum of the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)
def fib_gen(n):
    i=1
    if n==0:
        l=[]
    elif n==1:
        l=[1]
    elif n==2:
        l=[1,1]
    elif n>2:
        l=[1,1]
        while i<(n-1):
            l.append(l[i]+l[i-1])
            i+=1
    return(l)
n=int(input("Enter the number of Fibonnci numbers to generate"))
l=fib_gen(n)
print("The fibonacci sequence with {} elements is {}".format(n,l))
