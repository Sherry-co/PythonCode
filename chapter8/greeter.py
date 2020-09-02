# 函数的定义
def greet_user(username):
	""" 显示简单的问候 """
	print("Hello, " + username.title() + "!")
greet_user('jesse')

def get_formatted_name(first_name, last_name):
	"""返回整洁的姓名 """
	full_name = first_name + ' ' + last_name
	return full_name.title()
while True:
	print("\nPlease tell me your name:")
	print("(enter 'q' at any time to quit)")
	
	f_name = input("First name: ")
	if f_name == 'q':
		break
	l_name = input("Last name: ")
	if l_name == 'q':
		break
	formatted_name = get_formatted_name(f_name, l_name)
	print("\nHello! " + formatted_name + "!")