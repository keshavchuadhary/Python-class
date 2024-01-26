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

def function(number):
   y=number**2+5*number+2
   print(y)