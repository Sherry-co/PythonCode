# 从文件中读取数据
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    # print(contents)
    # 此时输出结束后还会有个空行
    print(contents.rstrip())

# 创建一个包含文件各行内容的列表
filename = "pi_digits.txt"

with open(filename) as file_object1:
    lines = file_object1.readlines()

for line in lines:
    print(line.rstrip())

# 使用文件的内容 rstrip()
pi_string = ''
for line in lines:
    pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))

# strip() 删除了空格
pi_string1 = ''
for line in lines:
    pi_string1 += line.strip()
print(pi_string1)
print(len(pi_string1))
