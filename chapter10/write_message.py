# 写入文件
filename = 'programming.txt'
with open(filename, 'w') as file_object:
    file_object.write("I love programming.")
# 写入多行
with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I lover creating new games.\n")

# 附加到文件：给文件添加内容，不是覆盖原有的内容
filename = 'programming.txt'

with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")
