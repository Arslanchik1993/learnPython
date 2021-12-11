# All Glory belongs to God



#Mastering the for loop

alphabet = 'abcdefghijklmnopqrstuvwxyz'
#When you write a for loop it's important to differentiate when u write it with "in range" or without it

#simple for loop that prints a string and it's index 10 times (starting with 0)
# for i in range(10):
    # print(f"number:{i}")

#When there is no in range the loop gets the actal value
# for i in alphabet:
    # print(i)

#Loop that apparently has to changes values in our list into numbers but it doesn't cause TypeError: 'str' object does not support item assignment
# b = 0  
# for i in alphabet:
#     alphabet[i] = str(b)

#but let's try with a new empty string this doesn't wor either
# b = 0
# # c = ''
# for i in alphabet:
#     c[i] = str(b)
#     b = b + 1
#     print(c)


# simple program for making a list from your string.
# b = 0
# c = []
# c.extend([ ]) 
# for i in alphabet:
#     d = (f"{i}")
#     c.extend([d])
# print(c)

#a program for for turning alphabet into a list in reverse order
# a = -1
# c = []
# for i in range(len(alphabet)):
#     c.append(alphabet[a])
#     a = a -1
# print(c)

