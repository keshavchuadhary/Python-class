def multiplication_table(number):
    for i in range(1, 11):
        print(f"{number} *{i} = {number*i}")
number=int(input("Enter a Number "))
for i in range(10):
 multiplication_table(i)

