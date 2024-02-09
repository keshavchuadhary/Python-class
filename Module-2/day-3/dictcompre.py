grade = {
    "prabhat":55,
    "Sammer":80,
    "praj":99,
    "Hritveek":36,
    "abhinab":85
}

new_dict = {key: value for key,value in grade.items() if key[0]=="p"}
print(new_dict)
new_dict1 = {key: value/2 for key,value in grade.items() if value>70}
print(new_dict1)