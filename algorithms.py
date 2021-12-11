#linear search 
alphabet = 'abcdefghijklmnopqrstuvwxyz'

def linearSearch(list, target):
    for i in range(0, len(list)):
        if list[i] == target:
            return i
a = linearSearch(alphabet, 'z')
print(a )