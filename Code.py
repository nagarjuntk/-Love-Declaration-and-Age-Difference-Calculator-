#Take input Boy_name
boy_name=input("Boy Name: ")

#Take input Boy Age
boy_age=int(input(" Boy Age: "))

#Take input Girl Name
girl_name=input("Girl Name: ")
#Take input Girl Age
girl_age=int(input("Girl Age:"))

#Concat  Boy Name With Declare Loves  Girl Name
print(boy_name + " loves " + girl_name)
 
# find the Differnt between age of them
age_diff= boy_age - girl_age

#format Concat Boy Name With Declare Loves  Girl Name AND find the Differnt between age of them
print(f"{boy_name} loves {girl_name}.  Age Differance is {age_diff}")