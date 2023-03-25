"""
Tracker Interface
allows users to perform CRUD operations on transactions database
"""
from transaction import *
import datetime

def print_commands():
    ''' Print all available commands. '''
    print('''
    0. quit
    1. show categories
    2. add category
    3. modify category
    4. show transactions
    5. add transaction
    6. delete transaction
    7. summarize transactions by date
    8. summarize transactions by month
    9. summarize transactions by year
    10. summarize transactions by category
    11. print this menu
    ''')

def print_transactions(response):
    """ Prints transaction responses with tuple containing diction of transaction details """
    if len(response)==0:
        print('no tasks to print')
        return
    print()
    print("%-10s %-10s %-15s %-15s %-15s"%('item #', 'amount','category','date','description'))
    print('-'*80)
    for values in response:
        values = (str(values['item #']), str(values['amount']), str(values['category']), values['date'], values['description'])
        print("%-10s %-10s %-15s %-15s %-15s" % values)
    print('-'*80)
    print()

def validate_date(date):
    """ Verifies whether the given date is in correct format """
    try:
        datetime.date.fromisoformat(date)
        return True
    except ValueError:
        return False
    
def print_categories(response):
    """ prints all categories in categories table """
    if len(response) == 0:
        print('no tasks to print')
        return
    print()
    print("%-20s %-20s"%('index', 'name'))
    print('-'*40)
    for values in response:
        values = (str(values['id']), values['name'])
        print("%-20s %-20s" % values)
    print('-'*40)
    print()

def get_category_index(transaction):
    """ asks the user to select a category when creating a transaction """
    index = -1
    invalid = True
    print("Select category index for transaction: ")
    existing_cate = transaction.show_categories()
    print_categories(existing_cate)
    while invalid:
        try:
            index = int(input("> "))
            if index < 1 or index > len(existing_cate):
                print("!!! That index does not exist !!!")
            else:
                invalid = False
        except ValueError:
            print("!!! Invalid Input !!!")
    return index

def add_transaction(transaction):
    """ Asks to enter transaction details and validates field entries """
    invalid = True
    while invalid:
        category_index = get_category_index(transaction)
        print("Enter transaction details (amount;date(YYYY-MM-DD);description):")
        details_str = input("> ")
        details_arr = details_str.split(";")
        try:
            if len(details_arr) < 3 or len(details_arr) > 3:
                print("!!! Missing or extraneous entry items !!!")
                raise ValueError
            amount = float(details_arr[0])
            if amount <= 0:
                print("!!! Invalid Amount !!!")
                raise ValueError

            date_str = details_arr[1].replace(" ", "")
            if validate_date(date_str) is False:
                print("!!! Invalid Date !!!")
                raise ValueError
            date = date_str

            description = details_arr[2].strip()

            details = { 'amount': amount, 'category': category_index, 'date': date, 'description': description }
        except ValueError:
            print("!!!!!!!!!!!!!!!!!!!!!")
        else:
            transaction.add_transaction(details)
            invalid = False
            print()
            print("Transaction Entry Successful!")
            print()

def add_category(transaction):
    """ Print existing categories and ask to enter new category """
    print("Categories")
    print_categories(transaction.show_categories())
    invalid = True
    while invalid:
        print("Enter new category:")
        cate_str = input("> ")
        cate_str = cate_str.replace(" ", "").upper()
        if transaction.check_category_exists(cate_str):
            print("!!! That category already exists !!!")
            print("Create a new category? (y/n): ")
            res = input("> ")
            res = res.strip().lower()
            if res == "n":
                invalid = False
        else:
            print()
            transaction.add_category(cate_str)
            print("New Category Saved!")
            print()
            invalid = False

# REPL 
# Loop to interact with Tracker
trans = Transaction(input("Enter filename of database you would like to interact with (omit the .db extension): ") + '.db')
print_commands()
interface_active = True
while interface_active:
    option = input("Enter Option # (11 to view options) > ")
    try:                                  # catch string to integer conversion errors
        option = int(option)
    except ValueError:
        print("!!! Invalid Option # !!!")
    else:
        if option < 0 or option > 11:
            print("!!! Invalid Option # !!!")
        else:
            if option == 0:
                interface_active = False
            elif option == 1:
                print("Show Categories")        # print all categories
                print_categories(trans.show_categories())
            elif option == 2:
                print("Add Category")
                add_category(trans)
            elif option == 3:
                print("modify category")
            elif option == 4:
                print("Transactions")
                print_transactions(trans.show_transactions())
            elif option == 5:
                print("Add Transaction")
                add_transaction(trans)
            elif option == 6:
                print("delete transaction")
            elif option == 7:
                print("summarize transactions by date")
            elif option == 8:
                print("summarize transactions by month")
            elif option == 9:
                print("summarize transactions by year")
            elif option == 10:
                print("summarize transactions by category")
            else:
                print_commands()
