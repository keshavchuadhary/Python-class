A = [1,2,3,4,56,6,7,7,77,5,4,4,3,2,2,2]
C = [element+3 for element in A]
print(C)
B = [element for element in A if element % 2 == 0]
print(B)
