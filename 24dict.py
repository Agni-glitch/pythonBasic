#ordered
dic={
    "name":"agni",
    "roll":16900323022,
    "course":"BTech",
    101:"CSE"
}
# print(dic["name2"])#error
print(dic.get('name2'))#None
print(dic.get('name'))#agni
print(dic.keys())#dict_keys(['name', 'roll', 'course', 101])
print(dic.values())#dict_values(['agni', 16900323022, 'BTech', 'CSE'])
for key in dic.keys():
    print(f"{key} has {dic[key]}")
# name has agni
# roll has 16900323022
# course has BTech
# 101 has CSE
print(dic.items())#dict_items([('name', 'agni'), ('roll', 16900323022), ('course', 'BTech'), (101, 'CSE')])
for key,value in dic.items():
    print(f"{key} has {value}")