login = input("Login Name: ")
password = input("Password: ")

initial = input("To lock your computer, type in lock: ")

command = ""
input1 = ""
input2 = ""
while command != initial:
	command=input ("Enter Command here: ")
count = 1
maxcount = 3
input1 = input("Login Name: ")
input2 = input("Password: ")
print ("                                ")
while (input1 != login or input2 != password) and count < maxcount:
	count = count + 1
	print ("Either your login name or password was incorrect. You have " 		+repr(maxcount-count+1) + " tries remaining.")
	input1 = input("Login Name: ")
	input2 = input("Password: ")
	print ("                               ")
if count > maxcount or (input1 != login and input2 != password):
	print("Sorry you cannot enter")
else: 
	print("Welcome back to your computer")
input("Press<enter>")