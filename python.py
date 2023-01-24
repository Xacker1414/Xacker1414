# file = open("text.txt")
# print(file.readlines())

# file = open("text.txt")
# print(file.readline())
# print(file.readline())

# with open("text.txt", "a+") as file:
# 	file.write("hello world !")
# 	file.seek(0)
# 	print(file.read())


# print(file.closed)



# with open("text.txt", "w+") as file:
# 	file.write("hello world !")
# 	print(file.tell())
# 	file.seek(0)
# 	print(file.read())

# count = 0
# with open("text.txt") as file:
# 	for i in file:
# 		count +=1
# 		print(i)



# with open("text.txt") as f:
# 	new_f = f.readlines()
# 	print(new_f)
# 	y = 0
# 	for i in new_f:
# 		y += len(i.split())
# 	print(y)




# with open("text.txt", "a+") as file:
# 	file.write("14142536987")
# 	file.seek(0)
# 	print(file.read())


# with open("text.txt") as file:
# 	print(file.readlines())
# 	for j in readlines:
# 		if len(j) <= 4:
# 			print(j)


# file = open("text.txt", "r")
# print(file.read(2))  


# import json
# python_obj = {
#   "name": "David",
#   "class":"I",
#   "age": 17 
# }
# print(type(python_obj))
# j_data = json.dumps(python_obj)

# print(j_data)  5


# def longest_word(filename):
#     with open("text.txt", 'r') as file:
#               words = file.read().split()   
#     max_len = len(max(words, key=len))
#     return [word for word in words if len(word) == max_len]

# print(longest_word('text.txt'))


# import json
# json_obj =  '{ "Name":"David", "Class":"I", "Age":6 }'
# python_obj = json.loads(json_obj)
# print("\nJSON data:")
# print(python_obj)
# print("\nName: ",python_obj["Name"])
# print("Class: ",python_obj["Class"])
# print("Age: ",python_obj["Age"]) 



# import json
# with open("text.json") as file:
# 	x = json.load(file)
# 	y = json.dumps(x)
# 	print(type(y))


