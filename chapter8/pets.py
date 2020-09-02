# 位置实参
def describe_pet(animal_type, pet_name):
	"""显示宠物的信息"""
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')

# 关键字实参 （无需考虑函数调用的实参顺序）
describe_pet(animal_type='hamster', pet_name = 'jerry')

# 使用默认值时，在形参列表中必须先列出没有默认值的形参，再列出有默认值的实参。
# 这让Python依然能够正确地解读位置实参。
def describe_pets(pet_name, animal_type='dog'):
	"""显示宠物的信息""" 
	print("\nI have a " + animal_type + ".") 
	print("My " + animal_type + "'s name is " + pet_name.title() + ".")

# 一条名为Willie的小狗
describe_pets('willie') 
describe_pets(pet_name='willie') 

# 一只名为Harry的仓鼠
describe_pets('harry', 'hamster') 
describe_pets(pet_name='harry', animal_type='hamster') 
describe_pets(animal_type='hamster', pet_name='harry')
