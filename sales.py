import sys
import random
import pyfiglet
from colorama import Fore,Style
import os
all_col= [Style.BRIGHT+Fore.RED, Style.BRIGHT+Fore.YELLOW, Style.BRIGHT+Fore.LIGHTBLUE_EX, Style.BRIGHT+Fore.LIGHTCYAN_EX,Style.BRIGHT+Fore.LIGHTMAGENTA_EX,Style.BRIGHT+Fore.LIGHTYELLOW_EX]

ran = random.choice(all_col)

def banner():
        os.system("clear")

        print(ran, pyfiglet.figlet_format("Sales\nManager"))
        print(ran + "\n\t\tV_1.2\t\n\n")

        print(Fore.CYAN, "- " * 4, " [+] Follow me on Instagram @saadkhan041 ", "- " * 4)
        print(Fore.LIGHTYELLOW_EX, "\n", "- " * 4, " [+] Follow me on Instagram @coding_memz ", "- " * 4)
        print(Fore.LIGHTRED_EX, "\n", "- " * 4, "[+] Github: https://github.com/Saadkhan041/ ", "- " * 3)


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
    file.write("\nName: " + name)
    file.write(f"\nDate: {datetime.datetime.today()}")
    file.write("\nTime: "+ datetime.datetime.today().strftime("%T"))

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

        file.write(f"price of {t} Kg of {q} is: {r * t}\n")


        total.append(k)

    print(f"Total is: {sum(total)}\n\n\t" + "File sales.txt is updated successfully!")

    file.write(f"Total is :{sum(total)}")
    file.write("\n" + "-" * 20 + "\n")
    print("\nSave all details in sales.txt")

cont =" "
while cont != "n" and "no":
    print(Fore.LIGHTYELLOW_EX + "\n\t\t[1] Perform sale\n\t\t[2] Exit\n ")

    choice = input(ran + "Enter your choice: ")
    if choice == "1":
        sales()
    elif choice == "2":
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







