

number_chosen= int(input(" Enter your number"))
 
modulenumberof3 = number_chosen % 3
modulenumberof5 = number_chosen % 5
 
if modulenumberof3 == 0 and modulenumberof5 == 0 :
     print("fizzbuzz")
elif modulenumberof5 == 0 :
     print("Buzz")
elif modulenumberof3 == 0 :
    print("fizz")

print(number_chosen)

#How to refactor this code 
#How to improve variable names 