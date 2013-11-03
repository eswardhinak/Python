beer = int(input("Number of beers in the beginning: "))
while beer >0:
	print(repr(beer) + " bottles of beer on the wall " + repr(beer) + "bottles of beer. Take one down. Pass it around. " + repr(beer-1) + " bottles of beer on the wall")
	beer = beer -1
