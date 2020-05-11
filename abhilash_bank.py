import random
from os import system,name
login_name="abhilash"
login_password="007"
def master():
    print("master")
    system('cls')
    print("you can Access any variable from here!".capitalize())
    print("\n\t1.previous user details\n\t2.new user details\n\t3.exit")
    choice=input("make a choice: ")
    if choice=="1":
        def previous_user_details(login_name,login_password,in_dep):
            print("\n\t1.User name\n\t2.password\n\t3.balance\n\t4.terminate account\n\t5.exit")
            choice=input("make a choice: ")
            if choice=="1":
                print("user name: "+login_name)
                print("\n\t1.change username\n\t2.exit")
                choice=input("make your choice: ")
                if choice=="1":
                    login_name=input("enter the new user name: ")
                    previous_user_details(login_name,login_password,in_dep)
                else:
                    previous_user_details(login_name,login_password,in_dep)

            elif choice=="2":
                print("password: "+login_password)
                print("\n\t1.change password\n\t2.exit")
                choice=input("make a choice: ")
                if choice=="1":
                    login_password=input("enter the new password: ")
                    previous_user_details(login_name,login_password,in_dep)
                else:
                    previous_user_details(login_name,login_password,in_dep)
            elif choice=="3":
                print("balance: "+in_dep)
                print("\n\t1.change balance \n\t2.exit")
                choice=input("make a choice: ")
                if choice=="1":
                    in_dep=input("enter the new balance: ")
                    previous_user_details(login_name,login_password,in_dep)
                else:
                    previous_user_details(login_name,login_password,in_dep)
            elif choice=="4":
                print("account terminated")
                login_name=""
                login_password=""
                in_dep="0"
                previous_user_details(login_name, login_password,in_dep)
            elif choice=="5":
                master()
            else:
                master()

    elif choice=="2":
        def new_user_details(name, acc_num, in_dep):
            print("\n\t1.User name\n\t2.password\n\t3.balance\n\t4.terminate account\n\t5.exit")
            choice = input("make a choice: ")
            if choice == "1":
                print("user name: " +name)
                print("\n\t1.change username\n\t2.exit")
                choice = input("make your choice: ")
                if choice == "1":
                    login_name = input("enter the new user name: ")
                    new_user_details(login_name, acc_num, in_dep)
                else:
                    previous_user_details(name, acc_num, in_dep)

            elif choice == "2":
                print("password: " +acc_num)
                print("\n\t1.change password\n\t2.exit")
                choice = input("make a choice: ")
                if choice == "1":
                    login_password = input("enter the new password: ")
                    previous_user_details(name, acc_num, in_dep)
                else:
                    new_user_details(name, acc_num, in_dep)
            elif choice == "3":
                print("balance: " + in_dep)
                print("\n\t1.change balance \n\t2.exit")
                choice = input("make a choice: ")
                if choice == "1":
                    in_dep = input("enter the new balance: ")
                    new_user_details(name, acc_num, in_dep)
                else:
                    new_user_details(name, acc_num, in_dep)
            elif choice == "4":
                print("account terminated")
                name = ""
                password = ""
                in_dep = 0
                new_user_details(name, acc_num, in_dep)
            elif choice == "5":
                master()
            else:
                master()

    elif choice=="3":
        start()
    else:
        print("make a correct choice")
        master()

def start():
   print("welcome to abhilash bank".capitalize())
   print("\n\t1.enter the bank\n\tX.master option")
   entry=input("enter your choice: ")
   if entry=="x":
       master()
   elif entry=="1":
       open_acc()
   else:
       print("make the right option")
       start()


def open_acc():
    print("\n\t1.login account\n\t2.Create account\n\t3.Quit bank")
    option=input("make your choice: ")
    if option=="1":
        login_acc()
    elif option=="2":
        create_acc()
    elif option == "3":
        start()
    else:
        print("wrong option \n\ttry again ")
        open_acc()
def login_acc_pass():
    login_password = input("enter your password: ")
    if login_password == "007":
        open_account(in_dep)
    else:
        print("wrong password!\n\ttry again")
        login_acc_pass()

def open_account(in_dep):
    print("\t1.check balance\n\t2.withdraw money\n\t3.deposit money\n\t4.exit account")
    choice=input("make a choice: ")
    if choice=="1":
        print("balance: "+str(in_dep))
        open_account(in_dep)
    elif choice=="2":
        print("balance"+str(in_dep))
        withdraw=int(input("how much do you withdraw: "))
        in_dep=int(in_dep)-withdraw
        print("balance: "+str(in_dep))
        open_account(in_dep)
    elif choice=="3":
        deposit=int(input("enter the deposit money: "))
        in_dep=int(in_dep)+deposit
        open_account(in_dep)
    elif choice=="4":
        print("exit account")
        open_acc()
    else:
        print("wrong choice")
        open_account(in_dep)


def create_acc():
    name = input("\nenter your username: ")
    try:
     age = int(input("enter your age: "))
    except:
        print("enter integer not string")
        create_acc()
    def acc_make_choice():
        typeof=input("\n1.personal account\n2.mutual account\n\tenter your choice:")
        if typeof=="1":
            print("you choice personal account")
            if age<18 :
                print("your are not eligible of personal account")
                acc_make_choice()
            else:
                print("account has been created")

        elif typeof=="2":
            print("you choice mutual account")
            mut_par_name=input("enter your partners name: ")
            try:
               mut_par_age=int(input("enter your partners age: "))
            except:
                print("enter integer not string ")
                acc_make_choice()
        else:
            print("wrong choice make the correct one")
            acc_make_choice()
    acc_make_choice()
    in_dep=int(input("enter initial deposit: "))
    acc_num = random.randint(100,9000)
    print("account number:"+str(acc_num))
    open_account(in_dep)
def login_acc():
    login_name=input("enter your user name: ")
    if login_name=="abhilash":
        login_acc_pass()


    else:
        login_acc()

start()




