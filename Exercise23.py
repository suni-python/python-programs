#Read a file of numbers and store it in a list
with open("primenumbers.txt",'r') as fp:
    l=[int(x) for x in fp.read().split('\n')]
with open("happynumbers.txt",'r') as fh:
    h=[int(x) for x in fh.read().split('\n')]
x=[x for x in l if x in h]
print("The common elements in both list ",x)
