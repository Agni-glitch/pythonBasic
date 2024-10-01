agni = True
print(agni:=False)

foods = list()
while True:
    if((food:=input("enter a food: ")).lower()=='nothing'):
        break
    foods.append(food)
print(foods)