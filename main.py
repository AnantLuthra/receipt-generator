from rich import print
from rich.console import Console

console = Console()

def add_account():
    """
    This function makes new account for the user
    """
    
    # Opening file for adding up the account.
    with open("details.txt", "a") as f:
        id = console.input("Enter your id: ")
        password = console.input("Enter your password: ")
        f.write(f"{id},{password}\n")
        console.print("Your account was created sucessfully !!", style="bold white")

def check_in():
    """
    This function checks that following id and password of user is valid.
    """
    with open("details.txt", "r") as f:
        data = f.read()
        data2 = data.split("\n")
        detail = {i.split(",")[0]:i.split(",")[1] for i in data2 if i.split(",")[0] != ""}

    id = console.input("Enter your [bold blue]id[/bold blue] and [bold blue]password[/bold blue]\nid: ")
    password = input("Password: ")

    for idd, passw in detail.items():
        if idd == id and passw == password:
            return True

    return False

def receipt_generator():
    """
    Main function of 
    """
    items = []
    prices = []
    

    if not check_in():
        console.print("Your creditials [bold red]not[/bold red] seems to be present before.")
        if console.input("Do you want to make your [bold green]new account[/bold green]? (y/n): ") == "y":
            add_account()
        else:
            return
    console.print("Login Sucessfull :white_check_mark:", style="bold green")

    print("Enter the name of item and price seperating each other by a '-' eg- 'Tomato-56'")
    print("Enter 'q' at the place of items to stop item adding in receipt.")
    try:
        while True:
            a = input()
            if a == 'q':
                break
            else:
                items.append(a)

        print("Baker store\n")

        if items == []: print("0 items entered."); return
        for item in items:
            b = item.split("-")
            item = b[0]
            price = b[1]
            prices.append(price)
            print(f"[bold white]Item[/bold white] = [bold yellow]{item}[/bold yellow], [bold purple]{price}[/bold purple]")
        n = 0
        for item in prices:
            item = int(item)
            n += item
        print(f"[bold blue]Total[/bold blue] = {n}\n")
        if n > 0:
            print("[bold green]Thanks for doing shopping from our shop :)[/bold green]")
    except Exception as e:
       print("\n[bold red]Oops[/bold red]! Something went [bold red]wrong[/bold red] !!")


print("Welcome to Receipt Generator.")
receipt_generator()