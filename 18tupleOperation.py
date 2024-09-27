countries= ("Spain","India","Italy","England","Germany")
temp = list(countries)
temp.append("Russia")
temp.pop(3)
temp[2]="Norway"
countries=tuple(temp)
print(countries) #('Spain', 'India', 'Norway', 'Germany', 'Russia')

countries2=("Portugal","Sweden","Georgia","Solvakia","Georgia")
temp=list(countries)
temp.pop(1)
countries=tuple(temp)
europianCountries=countries+countries2
print(europianCountries) #('Spain', 'Norway', 'Germany', 'Russia', 'Portugal', 'Sweden', 'Georgia',' Solvakia', 'Georgia')

res = europianCountries.count("Georgia")
print(res) #2