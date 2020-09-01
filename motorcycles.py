motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)

motorcycles_1=[]
motorcycles_1.append('honda')
motorcycles_1.append('yamaha')
motorcycles_1.append('suzuki')

# method insert()
print(motorcycles_1)
motorcycles_1.insert(0,'dacati')
motorcycles_1.insert(3,'yadi')
print(motorcycles_1)

#delete del
del motorcycles_1[0]
print(motorcycles_1)

# method pop()
motorcycles_2 =['honda', 'yamaha','suzuki']
print (motorcycles_2)

popped_motorcycle = motorcycles_2.pop()
print (motorcycles_2)
print (popped_motorcycle)

last_owned = motorcycles_2.pop()
print("The last motorcycle I owned was a " + last_owned.title() + ".")

motorcycles_3 = ['honda','yamaha','suzuki']
first_owned = motorcycles_3.pop(0)
print("The first motorcycle I owned was a " + first_owned.title() + ".")

#delete element by value --remove()
motorcycles_4 = ['honda','yamaha','suzuki','ducati']
print(motorcycles_4)
#motorcycles_4.remove('ducati')
#print(motorcycles_4)
too_expensive = 'ducati'
motorcycles_4.remove(too_expensive)
print(motorcycles_4)
print("\nA " + too_expensive.title() + " is too expensive for me.")
