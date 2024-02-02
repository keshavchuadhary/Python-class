A = [1,-2,3,4,-56,6,-7,7,-77,5,4,-9,3,2,2,2]
positive_list = []
negative_list = []
positive_list=[element for element in A if element>0]
negative_list=[element for element in A if element<0]
print(positive_list,negative_list)
print(max(positive_list))
positive_list.sort()