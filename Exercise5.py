

#write a program that returns a list that contains only the elements that are common between the lists (without duplicates).
import random

l1=random.sample(range(100),10)
l2=random.sample(range(100),10)
com_list=[x for x in l1 if x in l2]
print("Random List 1:",l1)
print("Random List 2:",l2)
print("The common elements:",com_list)







