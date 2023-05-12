stock={}
def show_manager_menu():
    print("Fruit Market Manager")
    print("1) Add Fruit Stock")
    print("2) view fruit stock")
    print("3) update fruit stock")

    choise_manager=int(input("enter your choise: "))
    if choise_manager==1:
        add_fruit()
        repeat()
    elif choise_manager==2:    
        view_fruit()
        repeat()
    elif choise_manager==3:
        update_fruit()
        repeat()
    else:
        print("Invalid Choise") 
def repeat():
    rc = input("do you want to perform more operation: press 'Y' for yes and 'N' for NO: ")   
    if rc == 'y' or rc == 'Y':
        print(show_manager_menu)
    elif rc == 'n' or rc == 'N':
        print(" thanks for using")

def add_fruit():
    print(" ADD FRUIT STOCK")
    fruit_name=int(input("enter frit name: "))
    qty =int(input("enter your qty(in kg): "))
    price=int(input("enter price: "))
    demo = {}
    demo.update({'qty':qty,'price':price})
    stock.update({fruit_name:demo})

def view_fruit():
    print(stock)

def update_fruit():
    fruitname=input("which fruit you want to update: ")
    temp=stock.get(fruitname)
    if temp==None:
        print("not exist")
        update_fruit()
    uc=int(input("what do you want to update:\n1)price\n2)quantity"))
    if uc==1:
        nprice=int(input("enter new price"))
        temp.update({'price': nprice})
        stock.update({fruitname: temp})
        repeat()
    elif uc == 2:
        nqty=int(input("enter new qty"))
        temp.update({'qty': nqty})
        stock.update({fruitname: temp})
        repeat()
    else:
        print("invalid choise")
        repeat()