a = [1,2,3,4]

# a[:2] = [0]# slice assignment 
print(a)

a.__setitem__(0, 0)
print(a)