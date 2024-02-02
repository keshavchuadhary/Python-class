A = [1,2,3,4,56,6,7,7,77,5,4,4,3,2,2,2]
even_list = []
odd_list = []
for i in A:
    if i % 2 == 0:
        even_list.append(i)
    else:
        odd_list.append(i)

print(even_list)
print(odd_list)
