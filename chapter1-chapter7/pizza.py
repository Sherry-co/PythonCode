# 嵌套
# 在字典中存储列表
pizza = {
	'crust': 'thick',
	'toppings': ['mushrooms', 'extra cheese'],
	}
# 概述所点的披萨
print("You ordered a " + pizza['crust'] + "-crust pizza " + 
	"with the following toppings:")
for topping in pizza['toppings']:
	print("\t" + topping)
