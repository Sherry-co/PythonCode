# 用户输入：函数input()（将用户输入解读为字符串）
message = input("Tell me something,and I will repeat it back to you:")
print(message)
# 多行字符串的创建 
prompt = "If you tell us who you are, we can personlize the message you see."
prompt += "\nWhat is your first name?"
prompt +="\nEnter 'quit' to end the program."
message = ""
while  message !='quit':
	message = input(prompt)
	print(message)
