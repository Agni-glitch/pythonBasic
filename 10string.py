name = "agni"

year = '1st year 2nd sem'

remark='i love football,"but i don\'t love polo".' #we can use "" inside '' or vise versa

print("my name is: ",name + year) #we can use + instead of , but , gives the space

string =""" Python is one of the most demanded programming languages in the job market.
Surprisingly," it is equally easy to learn and master  Python."
This python tutorial for absolute beginners in Hindi series will focus on teaching you python concepts from the ground up."""

#instead of """ we can use ''' and also all ' and " in between the lines are included in it 

print(name[0]) #op= a
print(name[1]) #like an array of characters
#print(name[6]) #index error
#useing a for loop to print a string
for character in remark: #to write a string vertically
    print(character)
    
print(len(remark)) #length of a string
print(remark[0:14]) #to write specific part