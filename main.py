
current_year = 2021
year_of_birth = 1988
user_name = 'John'
user_surname = 'Smith'
qwe = current_year-year_of_birth
print(qwe)

x = 152
y = 132
number = (int(((x % y) * 13) ** 0.5))


code_1 = '354'
code_3 = 132
code_2 = number

ver = "Hello Mary Gold. You are 26 years old. Your secret code is:" + code_1 + '-' + str(code_2) + '-' + str(code_3)
print(ver)

# Write a code to return "Hero" from given string
example_string1 = "Hello bro"
print(example_string1[0:2] + example_string1[7:9])
print(example_string1.replace("Hello b","He"))

# Write a code to return "Jack is my name"
example_string2 = "jack Is My NAME"
print(example_string2.capitalize())

# Write a code to return "Get rid of stars please"
example_string3 = "*Get rid of stars please*"
text = example_string3.strip("*")
print(text)

# Write a code to return "Hello my name is Jack"
example_string4 = "hello my name is jack"
print(example_string4[0].upper() + example_string4[1:16] + example_string4[17].upper() + example_string4[18:25])


# Write a code to return formatted string "Hello, my name is Jack"
var1 = " jack"
var2 = "hello"
var3 = " MY NAME IS"
print(var2.capitalize() + var3.lower() + var1.capitalize())

# Write a code to return byte_string text value
byte_string = b"\316\273"
decoded_string = byte_string.decode()
print(decoded_string)

# Write a code to return True if cost is greater than 500$
x = int(input("How much it costs?"))
if x == 500:
    print("its good price")
elif x < 500:
    print("its very cheep")
else:
    print("its more greater than 500")
