name = input("please enter your name...")
lastname = input('please enter last name..')
age = input('please enter your age..')
print("Hello", name, lastname+"!You are", age, "years old!")
print("Hello "+name+" "+lastname+"!You are "+str(age)+" years old!")

side_a=float(input("enter side A:"))
side_b=float(input("enter side B:"))
side_c=float(input("enter side C:"))

half_perimetr=(side_a+side_b+side_c)/2
triangle_area=(half_perimetr*(half_perimetr-side_a) * (half_perimetr-side_b) * (half_perimetr-side_c))**0.5
print("Result is:",triangle_area)
