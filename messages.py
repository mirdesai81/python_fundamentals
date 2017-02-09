message = "Languages:\nC\nJavascript\nAngularJs"
print(message)

message = " This is a test for python. "
print(message.strip())

value = 10 ** 3
print(value)

age = 35
print("Happy " + str(age) + "th Birthday!!!")

cycles = ['trek', 'kids', 'mountain']
print(cycles)
cycles.append('tri-cycle')
print(cycles[-1].title())
cycles.insert(1,'bicycle')
del cycles[1]
print(cycles)

cities = ['new york', 'san jose', 'paris', 'seville' , 'granada']
print(cities)
print(sorted(cities))
print(cities)
print(sorted(cities,reverse=True))
print(cities)

for city in cities:
    print("I love to visit" + city)

numbers = []
for num in range(1,12,2):
    numbers.append(num)

print(numbers)
print(list(range(1,10)))
print(numbers[1:4])
print(numbers[:4])
print(numbers[2:len(numbers)])
print(numbers[3:])
