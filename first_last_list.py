#Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list. For practice, write this code inside a function.
def get_list():
    print("ENter the number of elements in a list")
    return [int(x) for x in input().split()]

def first_last(lis):
    if lis:
        return [lis[0],lis[-1]]
    else:
        return []


lis=get_list()
new_lis=first_last(lis)
if new_lis:
    print("The new list with first and last element",new_lis)
else:
    print("you have entered a empty list")
