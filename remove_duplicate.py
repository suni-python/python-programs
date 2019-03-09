#Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.
#Write two different functions to do this - one using a loop and constructing a list, and another using sets.
def get_list():
    print("Enter a list of numbers with space apart")
    return [int(x) for x in input().split()]

def remove_duplicate(lis):
    l=[]
    for x in lis:
        if x not in l:
            l.append(x)
    return l

def remove_duplicate_set(lis):
    return list(set(lis))

lis=get_list()
new_lis=remove_duplicate(lis)
print("The original list is ",lis)
print("The new list without duplicates ",new_lis)
print("list without duplicates using set ",remove_duplicate_set(lis))

