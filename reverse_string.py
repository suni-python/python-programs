#Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order.
def reverse_string(st):
    lis=st.split()
    return lis[::-1]

st=input("Enter a multiple word sentence: ")
new_st=' '.join(reverse_string(st))
print("{} becomes {}".format(st,new_st))
