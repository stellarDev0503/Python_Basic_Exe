# 1.5.1 - Streamline Your Print Statements
# Solutions to review exercies


# Exercise 1
weight = 0.2
animal = "newt"

# Concatenate a number and a string in one print statement
print(str(weight) + " kg is the weight of the newt.")


# Exercise 2
# Use format() to print a number and a string inside of another string
print("{} kg is the weight of the {}.".format(weight, animal))


# Exercise 3
# Use formatted string literal (f-string) to reference objects inside a string
print(f"{weight} kg is the weight of the {animal}.")
