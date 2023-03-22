# Rose
# Prints out all the commands the user should be able to use
def print_commands():
    ''' Print all available commands. '''
    print('''0. quit
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
    11. print this menu''')

# Rose
# Input: user input split by whitespace
# Processes the argument list from the user's input and performs an sql command on the database using that input
# I feel like there's a better way to parse these commands. Feel free to change this
# TODO add calls to transaction to change the database
def process_args(arglist):
    # blank input
    if arglist==[]:
        print_commands()
    # quit
    elif arglist[0]=="quit":
        return
    # show categories/transactions
    elif arglist[0]=="show":
        if len(arglist)!= 2:
            print_commands()
        elif arglist[1]=="categories":
            '''TODO add transaction.py call'''
        elif arglist[1]=="transactions":
            '''TODO add transaction.py call'''
        else:
            print(arglist,"is not implemented")
            print_commands()
    # add category/transaction
    elif arglist[0]=="add":
        if len(arglist)!= 2:
            print_commands()
        elif arglist[1]=="category":
            '''TODO add transaction.py call'''
        elif arglist[1]=="transaction":
            '''TODO add transaction.py call'''
        else:
            print(arglist,"is not implemented")
            print_commands()
    # modify category
    elif arglist[0]=="modify":
        if len(arglist)!= 2:
            print_commands()
        elif arglist[1]=="category":
            '''TODO add transaction.py call'''
        else:
            print(arglist,"is not implemented")
            print_commands()
    # delte transaction
    elif arglist[0]=="delete":
        if len(arglist)!= 2:
            print_commands()
        elif arglist[1]=="transaction":
            '''TODO add transaction.py call'''
        else:
            print(arglist,"is not implemented")
            print_commands()
    # summarize transactions by date/month/year/category
    elif arglist[0]=="summarize":
        if len(arglist)!= 4:
            print_commands()
        if arglist[1]=="transactions" and arglist[2]=="by":
            if arglist[3]=="date":
                '''TODO add transaction.py call'''
            elif arglist[3]=="month":
                '''TODO add transaction.py call'''
            elif arglist[3]=="year":
                '''TODO add transaction.py call'''
            elif arglist[3]=="category":
                '''TODO add transaction.py call'''
            else:
                print(arglist,"is not implemented")
                print_commands()
        else:
            print(arglist,"is not implemented")
            print_commands()
    # print this menu
    elif len(arglist) == 3 and arglist[0]=="print" and arglist[1]=="this" and arglist[2]=="menu":
        '''TODO add transaction.py call'''
    else:
        print(arglist,"is not implemented")
        print_commands()

"""
# here is where we run the script
# first we get a connection to the database
con= sqlite3.connect(os.getenv('HOME')+'/todo.db')
cur = con.cursor()

# then we create the todo table if it doesn't exist
# and for completed we use 0 for False and 1 for True, as sqlite has not booleans
cur.execute('''CREATE TABLE IF NOT EXISTS todo
                    (title text, desc text, completed int)''')


# and finally we commit our changes and close the connection
con.commit()
con.close()