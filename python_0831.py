#if 判断语句
available_toppings = ['mushrooms','olives','green peppers','pepperoni','pineapple','extra cheese']
request_toppings = ['mushrooms','french fries','extra cheese']
for request_topping in request_toppings:
	if request_topping in available_toppings:
		print("Adding " + request_topping +".")
	else:
			print("Sorry, we don't have " + request_topping + ".")
print("\nFinished making your pizza! ")

