fruits = ['apple', 'orange', 'pear']
fruits.insert(0, "sand")

print(fruits)

a = [0, 98, 78]
b = [99,88,7890]

a.extend(b)

print(a)
print(b)

ls = ['apple', 'orange', 'pear', "destiny", "caleb"]
ls[1:3] = ["nico"]

print(ls)