import manager
import customer

def start():
    print("welcome to fruit market")
    print("1)Manager")
    print("2)Customer")

    role=int(input("enter your role"))

    if role == 1:
        manager.show_manager_menu()
    elif role==2:
        pass
    else:
        print("INVALID CHOISE") 

start()           
