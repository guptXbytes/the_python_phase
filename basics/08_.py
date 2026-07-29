fruits = ["apple", "lichi", "mango", "grapes", "pomogranate"]
print(fruits)
print(fruits[0])
print(fruits[-1])

fruits[1]="mango"
fruits.append("orange")
fruits.insert(2, "grapes")
fruits.remove("mango")
print(len(fruits))

for _ in fruits:
    print(_)