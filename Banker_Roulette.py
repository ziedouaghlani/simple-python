import random

names_string = input("Insert list of name seperated by a comma. \n")

names= names_string.split(",")

r=random.randint(0, len(names))

print ("The person chosen is: " + names[r] )
