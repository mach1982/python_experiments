

shopping_list = []

print("\t"+"#"*5 + "Instructions"+ "#"*5 + "\n")
print("Whatto ghet at the shop?")
print("Enter DONE to quit")

def show_list():
	shopping_list.remove("SHOW")

	for item in shopping_list:
	
		print(item)
		
		
def show_help():
	shopping_list.remove("HELP")
	print("SHOW will print of the list")
	print("HELP will display this menu ")

while True:
	
	new_item= input(">")
	shopping_list.append(new_item)
	
	if new_item =="SHOW":
		show_list()
		continue

	elif new_item =="HELP":
		show_help()
		continue
	
	elif new_item =="DONE":
		break
	
print("hers is your list")

shopping_list.remove("DONE")

for item in shopping_list:
	
	print(item)



	
