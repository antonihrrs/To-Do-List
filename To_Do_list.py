

to_do_list = []

def show_to_do_list():
    print("\nHere's your to do list :\n")
    for item in to_do_list:
        print(item)
    if not to_do_list:
        print("Your list is empty !\n")


show_to_do_list()
to_do_list.append(input("Add something to your to do list : ").lower())

show_to_do_list()

while True :
    ask_add_or_remove = input("\nDo you want to add or remove something from your list ?\n").lower()
    if ask_add_or_remove == "add":
        user_add = input("\nAdd : ").lower()
        to_do_list.append(user_add)
        show_to_do_list()
        print("\n")

    elif ask_add_or_remove == "remove" :
        show_to_do_list()
        print("\n")
        user_remove = input("\nWhat do you want to remove : ").lower()
        while True:
            if user_remove in to_do_list :
                to_do_list.remove(user_remove)
                show_to_do_list()
                print("\n")
                break

            elif user_remove not in to_do_list:
                print (f"Invalid request..., '{user_remove}' isn't on your list.")
                break
                

    else :
        print ("Invalid request")

        
