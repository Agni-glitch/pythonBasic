employee ={122:45,123:89,567:69,670:68}
ep2={222:67,566:90}

employee.update(ep2)
print(employee)#{122: 45, 123: 89, 567: 69, 670: 68, 222: 67, 566: 90}
employee.pop(222)
employee.popitem()
del employee[566]
employee.clear()#{}
empt={}#empty dict