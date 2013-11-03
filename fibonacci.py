
a = 0
b = 1
count = 0
max = int(input("length of sequence: "))
while count < max:
	count = count +1
	newa = a
	newb= b
	a = newb
	b = newb+newa
	print (newa)
input("Press<enter>")
