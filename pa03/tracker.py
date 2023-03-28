"""
Tracker Interface
allows users to perform CRUD operations on transactions database
"""
import datetime
import transaction as t_module

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

def print_transactions(response, database):
    """ Prints transaction responses with tuple containing diction of transaction details """
    if len(response)==0:
        print('no transactions to print')
        return
    print()
    print(f'{"item #":<10}{"amount":<10}{"category":<15}{"date":<15}{"description":<15}')
    print('-'*80)
    for values in response:
        values = (str(values['item #']), str(values['amount']),
        database.get_category(int(values['category'])), values['date'], values['description'])
        print(
            f'''{values[0]:<10}{values[1]:<10}{values[2]:<15}{values[3]:<15}{values[4]:<15}''')
    print('-'*80)
    print()

def validate_date(date):
    """ Verifies whether the given date is in correct format """
    try:
        datetime.date.fromisoformat(date)
        return True
    except ValueError:
        return False

##################### Customized print tables for the summarize commands #####################
def print_sum_by_date(response, database):
    """ prints summary of transactions by date """
    if len(response) == 0:
        print('no transactions to summarize')
        return
    print()

    print(
    f"""{'Date':<13}{'Category':<10}{'# of Transactions':<20}{'Sum of Transaction Amounts':<20}""")
    print('-'*75)
    for values in response:
        values = (str(values['date']), database.get_category(int(values['category'])),
        str(values['# of transactions']), values['sum of transaction amounts'])
        print(f"""{values[0]: <13}{values[1]: <10}{values[2]: <20}{values[3]:<20}""")
    print('-'*75)
    print()

def print_sum_by_month(response, database):
    """ prints summary of transactions by month """
    if len(response) == 0:
        print('no transactions to summarize')
        return
    print()
    print(
    f"""{'Month':<13}{'Category':<10}{'# of Transactions':<20}{'Sum of Transaction Amounts':<20}""")
    print('-'*75)
    for values in response:
        values = (str(values['month']), database.get_category(int(values['category'])),
        str(values['# of transactions']), values['sum of transaction amounts'])
        print(f"""{values[0]:<13}{values[1]:<10}{values[2]:<20}{values[3]:<20}""")
    print('-'*75)
    print()

def print_sum_by_year(response, database):
    """ prints summary of transactions by year """
    if len(response) == 0:
        print('no transactions to summarize')
        return
    print()
    print(
    f"""{'Year':<13}{'Category':<10}{'# of Transactions':<20}{'Sum of Transaction Amounts':<20}""")
    print('-'*75)
    for values in response:
        values = (str(values['year']), database.get_category(int(values['category'])),
        str(values['# of transactions']), values['sum of transaction amounts'])
        print(f"""{values[0]:<13}{values[1]:<10}{values[2]:<20}{values[3]:<20}""")
    print('-'*75)
    print()

def print_sum_by_category(response, database):
    """ prints summary of transactions by category """
    if len(response) == 0:
        print('no transactions to summarize')
        return
    print()
    print(
    f"""{'Category':<10}{'Date':<15}{'# of Transactions':<20}{'Sum of Transaction Amounts':<30}""")
    print('-'*80)
    for values in response:
        values = (database.get_category(int(values['category'])),
        str(values['date']), str(values['# of transactions']),
        str(values['sum of transaction amounts']))
        print(f"""{values[0]:<10}{values[1]:<15}{values[2]:<20}{values[3]:<30}""")
    print('-'*80)
    print()
##############################################################################################

def print_categories(response):
    """ prints all categories in categories table """
    if len(response) == 0:
        print('no categories to print')
        return
    print()
    print(f"{'Index': <20} {'Name': <20}")
    print('-'*40)
    for values in response:
        values = (str(values['id']), values['name'])
        print(f"{values[0]: <20} {values[1]: <20}")
    print('-'*40)
    print()

def get_category_index(transaction):
    """ asks the user to select a category """
    index = -1
    invalid = True
    print("Select category index (or -1 to cancel): ")
    existing_cate = transaction.show_categories()
    print_categories(existing_cate)
    while invalid:
        try:
            index = int(input("< "))
            if index == -1:
                return -1
            if index < 1 or index > len(existing_cate):
                print("!!! That index does not exist !!!")
            else:
                invalid = False
        except ValueError:
            print("!!! Invalid Input !!!")
    return index

def get_transaction_index(transaction):
    """ asks the user to select a transaction id when deleting a transaction """
    index = -1
    invalid = True
    print("Select transaction index to delete (or -1 to cancel): ")
    existing_trans = transaction.show_transactions()
    print_transactions(existing_trans, transaction)
    while invalid:
        try:
            index = int(input("> "))
            if index == -1:
                return -1
            if index < 1 or index > len(existing_trans):
                print("!!! That transaction id does not exist !!!")
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
        if category_index == -1:
            return
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

            details = { 'amount': amount, 'category': category_index,
            'date': date, 'description': description }
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


def delete_transaction(transaction):
    """ Print existing categories and ask to enter new category name """
    transaction_index = get_transaction_index(transaction)
    if transaction_index == -1:
        return
    transaction.delete_transaction(transaction_index)
    print()
    print("Transaction deleted.")
    print()


def modify_category(transaction):
    """ Print existing categories and ask to enter new category name """
    print("Categories")
    print_categories(transaction.show_categories())
    category_index = get_category_index(transaction)
    if category_index == -1:
        return
    invalid = True
    while invalid:
        print("Enter new category name:")
        new_name = input("> ")
        new_name = new_name.replace(" ", "").upper()
        if transaction.check_category_exists(new_name):
            print("!!! That category already exists !!!")
        else:
            print()
            trans.modify_category(category_index, new_name)
            print("Category Modified!")
            print()
            invalid = False

# REPL
# Loop to interact with Tracker
trans = t_module.Transaction(
    input("Enter filename of database you would like to interact with (omit the .db extension): ")
    + '.db')
print_commands()
INTERFACE_ACTIVE = True
while INTERFACE_ACTIVE:
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
                INTERFACE_ACTIVE = False
            elif option == 1:
                print("Show Categories")        # print all categories
                print_categories(trans.show_categories())
            elif option == 2:
                print("Add Category")
                add_category(trans)
            elif option == 3:
                print("Modify Category")
                modify_category(trans)
            elif option == 4:
                print("Transactions")
                print_transactions(trans.show_transactions(), trans)
            elif option == 5:
                print("Add Transaction")
                add_transaction(trans)
            elif option == 6:
                print("Delete Transaction")
                delete_transaction(trans)
            elif option == 7:
                print("summarize transactions by date")
                print_sum_by_date(trans.sum_by_date(), trans)
            elif option == 8:
                print("summarize transactions by month")
                print_sum_by_month(trans.sum_by_month(), trans)
            elif option == 9:
                print("summarize transactions by year")
                print_sum_by_year(trans.sum_by_year(), trans)
            elif option == 10:
                print("summarize transactions by category")
                print_sum_by_category(trans.sum_by_category(), trans)
            else:
                print_commands()
