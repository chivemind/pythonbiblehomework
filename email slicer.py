#get user email address

email = input("What is your email address?: ").strip()

# slice user name

user = email[:email.index("@")]

# slice domain name

domain = email[email.index("@")+1:]


# format message

string = "Your username is {} and your domain name is {}."
output = string.format (user, domain)

# display output message

print (output)

user = input("Create a username: ").strip()

password = input("Create a unique password: ").strip()

string = "Your username is {} and your password is {}."
output = string.format (user, password)

print (output)

address = input("Write your full street address: ").strip()

street = address[:address.index(",")]

city = address[address.index(",")+1:]

string = "You live at {} in{}."
output = string.format (street, city)

print (output)



