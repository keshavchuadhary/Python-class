def check_prime(number):
    counter = 0
    prime= False
    for i in range(1, number+1):
     if number % i == 0:
        counter = counter+1
    if counter == 2:
       prime=True
    return prime
        


def multiplication_table(number):
    for i in range(1, 11):
        print(f"{number} *{i} = {number*i}")
# number=int(input("Enter a Number "))
# for i in range(10):
#  multiplication_table(i)

number= int(input("Enter a number to check prime"))

if check_prime(number):
   multiplication_table(number)
   