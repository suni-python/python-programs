#Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password every time the user asks for a new password.
import random
import string
lis=list(string.ascii_letters+string.digits+string.punctuation)
n=int(input("Enter the length of password: "))
pass_word=random.sample(lis,n)
print("The new password is: ",''.join(pass_word))
