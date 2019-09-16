#Captain Rainbow Checklist Redo
checklist = list()

#CRUD (Create, Read, Update, Destroy)
#Create
def create(item):
    checklist.append(item)
#Read
def read(index):
    return checklist[index]
#Update
def update(index, item):
    checklist[index] = item
#Destroy
def destroy(index):
    checklist.pop(index)
#List all Items function
def list_all_items():
    index = 0
    for list_item in checklist:
        print("{} {}".format(index, list_item))
        index += 1
#Test function
def test():
    create("purple sox")
    create("red cloak")

    print(read(0))
    print(read(1))

    update(0, "purple socks")

    destroy(1)

    print(read(0))

    list_all_items()
# Mark Completed function
def mark_completed(index):
    update(index,"√" + checklist[index])
    print()

# Select function
def select(function_code):
    #Create Item
    if function_code == "C":
        input_item = user_input("Input item:")
        create(input_item)
    #Read Item
    elif function_code == "R":
        item_index = user_input("Index Number?")

        #Remember that item_index must actually exist or our program will crash.
        read(item_index)

    #Print all items
    elif function_code == "P":
        list_all_items()
    #Catch all
    else:
    print("Unknown Option")
    return True

#The input function will display a message in the terminal and wait for user input.
def user_input(prompt):
    user_inpute = input(prompt)
    return user_input
# test function
running = True
while running:
    selection = user_input(
    "Type C to create, R to read, and P to display current list."
    )
