grade = {
    "prabhat":55,
    "Sammer":80,
    "Praj":99,
    "Hritveek":36,
    "abhinab":85
}
new_dict = {}
# # print(grade.get("abhinab"))
# for key,value in grade.items():
#     if value > 70:
#         new_dict[key] = value
# print(new_dict)

new_dict1 = {}
new_dict2 = {}
for key,value in grade.items():
    if value % 2 == 0 :
        value+=1
        new_dict1[key] = value
    else:
        value+=1
        new_dict2[key] = value
print("odd",new_dict1)
print("even",new_dict2)


        
