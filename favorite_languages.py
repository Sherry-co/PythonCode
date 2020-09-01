favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}
	
print("Sarah's favorite language is " + 
	favorite_languages['sarah'].title() + 
	".")
	
print("\n")
for name,language in favorite_languages.items():
	print(name.title() + 
		"'s favorite language is " + 
		language.title() + 
		".")
print("\n")
for name in favorite_languages.keys():
	print(name.title())
	
print("\n")
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
	print(name.title())
	if name in friends:
		print(" Hi " + name.title() + 
			", I see your favorite language is " + 
			favorite_languages[name].title() + "!")
			
# 按顺序遍历字典中所有的键 sorted()
print("\n")
for name in sorted(favorite_languages.keys()):
	print(name.title() + ", thank you for taking the poll.")

# 遍历字典中所有的值
print("\n")
print("The following languages have been mentioned:")
for language in favorite_languages.values():
	print(language.title())

# 剔除字典中值的重复
print("\n")
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
	print(language.title())
# 嵌套 ： 字典中有列表嵌套
favorite_languages = {
	'jen': ['python', 'ruby'],
	'sarah': ['c', 'java'],
	'edward': ['ruby', 'go'],
	'phil': ['python', 'haskell'],
	}
for name,languages in favorite_languages.items():
	print ("\n" + name.title() + "'s favorite languages are: ")
	for language in languages:
		print("\t" + language.title())
