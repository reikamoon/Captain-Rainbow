#Captain Rainbow Checklist Redo
checklist = list()

#The input function will display a message in the terminal and wait for user input.
def user_input(prompt):
    user_inpute = input(prompt)
    return user_input
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
    
