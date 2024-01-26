from imp import check_prime,multiplication_table,function

number= int(input("Enter a number to check prime"))
if not check_prime(number):
   multiplication_table(number)
else:
   function(number)

   