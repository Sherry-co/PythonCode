# 传递列表

def greet_users(names):
	for name in names:
		msg = "Hello, " + name.title() + "!"
		print(msg)
usernames= ['tom', 'jerry' ,'zoe','jannie']
greet_users(usernames)
