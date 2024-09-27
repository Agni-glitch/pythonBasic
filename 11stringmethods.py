# strings are immutable but string methods returns a new string 
name ="Agni Roybar"
print(len(name)) #length function #11

print(name.upper()) #AGNI ROYBAR
print(name.lower()) #agni roybar

print(name.rstrip("r")) #only the trailing character #Agni Royba
print(name.replace("A","Ghu")) #if it not founds a character in string then its returns the same #Ghugni Roybar
print(name.split(" ")) #converts to a list #['Agni', 'Roybar']

thumnale= "NOt mY typE"
print(thumnale.capitalize()) #Not my type ,not effective when it is already in right form #Not my type
print(thumnale.center(100)) #add space in front #                                            NOt mY typE
print(len(thumnale)) #11
print(len(thumnale.center(100))) #only counts the space #100

name2= "the best is Agni Agni Agni dkjguykgjygk Agni"
print(name2.count("Agni")) #number of times it is repeated #4
print(name2.find("Agni")) #only considers the first occurance #12
print(name2.find("gcfj")) #returns -1 for no occurance #-1
print(name2.endswith("Ag")) #bool #False
print(name2.endswith("Ag",0,14)) #bool (from 0 to 14 of the string) #True

print(name2.index("Agni")) #same as find but declears error when there is no detection #12
print(name2.isalnum()) #returns true only when all characters are alphanumeric #False
print(name2.isalpha()) #returns true only when all characters are alphabets #False
print(name2.islower()) #returns true only when all characters are lower alphabets #False
print(name2.isupper()) #returns true only when all characters are upper alphabets #False
print(name2.isprintable()) #returns true only when all characters are printable they are not escape sequence or others # true in this case #True
print(name2.isspace()) #returns true only when line contains a space or tab #False
print(name2.istitle()) #it its a title returns true as the first letter of 1st word is upper alphabets #False
print(name2.startswith("the best")) #finds the start #True
print(name2.startswith("Agn",12,19)) #finds the starting #True
print(name2.swapcase()) #case are swap,upper to lower and lower to upper #THE BEST IS aGNI aGNI aGNI DKJGUYKGJYGK aGNI
print(name2.title())#converts to title #The Best Is Agni Agni Agni Dkjguykgjygk Agni
