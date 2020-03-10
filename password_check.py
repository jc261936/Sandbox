min_length = 4
password = input("Please enter a password with a minimum of 4 Characters- ")
while len(password) < min_length:
    password = input("Please enter a password with a minimum of 4 Characters- ")
stars = "*" * len(password)
print(stars)