#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

new_list1=[]
for x in range(1,nr_letters+1):
  l_list=random.choice(letters)
  new_list1.append(l_list)
new_list2=[]
for y in range(1,nr_symbols+1):
  s_list=random.choice(symbols)
  new_list2.append(s_list)
new_list3=[]
for z in range(1, nr_numbers+1):
  n_list=random.choice(numbers)
  new_list3.append(n_list)

final_list=new_list1+new_list2+new_list3
f_number=str("")
for number1 in final_list:
  f_number+=number1

y=final_list
random.shuffle(final_list)

final_number=str("")
for number2 in final_list:
  final_number+=number2

print(f"Here is your password: {final_number}")
  
