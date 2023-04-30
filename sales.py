import sys
import random
import pyfiglet
from colorama import Fore,Style
import os,datetime
all_col= [Style.BRIGHT+Fore.RED, Style.BRIGHT+Fore.YELLOW, Style.BRIGHT+Fore.LIGHTBLUE_EX, Style.BRIGHT+Fore.LIGHTCYAN_EX,Style.BRIGHT+Fore.LIGHTMAGENTA_EX,Style.BRIGHT+Fore.LIGHTYELLOW_EX]

ran = random.choice(all_col)

def banner():
    os.system("clear")

    print(ran, pyfiglet.figlet_format("\f\tSales\n\tManager"))
    print(ran + "\t\tV_2.7.0 'Final Release'\t\n\n")
    print("*" * 63)

    print(Style.BRIGHT + Fore.LIGHTCYAN_EX, "\n", "- " * 4, " [+] Follow me on Instagram @cyber_dioxide ", "- " * 4)
    print(Style.BRIGHT + Fore.LIGHTYELLOW_EX, "\n", "- " * 4, " [+] Follow me on Instagram @coding_memz ", "- " * 4)
    print(Style.BRIGHT + Fore.LIGHTRED_EX, "\n", "- " * 4, "[+] Github: https://github.com/Saadkhan041/ ", "- " * 3)
    print("\n", "*" * 63)

banner()

def exit():
    sys.exit()


item_price = []
item_name = []
per_item = []
total = []


def sales():
    name = input(Fore.LIGHTYELLOW_EX + "\nEnter name of customer: ")
    item_num = int(input(Fore.LIGHTBLUE_EX + "\nEnter quantity of items: "))
    file = open("sales.txt", "a+")
    file.write("\n\t\tName: " + name + "\n\n")
    file.write(f"\n\t\tDate: {datetime.date.today()}")
    file.write("\n\t\tTime: "+ datetime.datetime.today().strftime("%T") + "\n")


    for i in range(1, item_num + 1):
        ran = random.choice(all_col)
        num = input(ran + f"\nEnter name of item {i}: ")
        item_name.append(num)

    for q in item_name:
        ran = random.choice(all_col)
        n = input(ran + f"\nEnter price of 1Kg of {q}: ")
        n = float(n)

        item_price.append(n)

        amount = input(Fore.LIGHTMAGENTA_EX + f"Enter amount of {q} in grams: ")
        amount = float(amount)
        amount = amount / 1000
        per_item.append(amount)

        for r in item_price:
            r = float(r)

            for t in per_item:
                t = float(t)
            k = r * t
        print(ran + f"price of {t} Kg of {q} is: {r * t}\n")

        file.write(f"\nprice of {t} Kg of {q} is: {r * t}\n")


        total.append(k)

    print(f"Total is: {sum(total)}\n\n\t" + "File sales.txt is updated successfully!")

    file.write(f"\nTotal is :{sum(total)}")
    file.write("\n" + "-" * 50 + "\n")
    print("\nSaved all details in sales.txt")

def view():
    file = open("sales.txt", "r")
    print(ran + "\n\tThis is what i've found!\n")

    print(all_col[2%6] + file.read())


cont =" "
while cont != "n" and "no":
    print(Fore.LIGHTYELLOW_EX + "\n\t\t[1] Sales Manager\n\t\t[2] Check Database\n\t\t[3] Exit\n ")

    choice = input(ran + "Enter your choice: ")
    if choice == "1":
        sales()

    elif choice == "2":
        view()

    elif choice == "3":
        print(ran + "\n\tDont Forget to do following tasks :-)\t\n")
        print(Fore.CYAN, "- " * 4, " [+] Follow me on Instagram @saadkhan041 ", "- " * 4)
        print(Fore.LIGHTYELLOW_EX, "\n", "- " * 4, " [+] Follow me on Instagram @coding_memz ", "- " * 4)
        print(Fore.LIGHTRED_EX, "\n", "- " * 4, "[+] Github: https://github.com/Saadkhan041/ ", "- " * 3)
        exit()

    else:
        print(ran + "\nInvalid option")
        exit()
    cont = input(ran + "\nDo you want to continue? [y/n]:")

    if cont == "y":
        os.system("clear")
        banner()







