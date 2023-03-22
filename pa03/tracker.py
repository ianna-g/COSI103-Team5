import sqlite3
import sys
import os


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

def print_todos(todos):
    ''' print the todo items '''
    for item in todos:
            print("item #%-3s: %-10s %30s %2d"%item)

def process_args(arglist):
    if arglist==[]:
        print_commands()
    elif arglist[0]=="quit":
        return
    elif arglist[0]=="show":
        if len(arglist)!= 2:
            print_commands()
        elif arglist[1]=="categories":
            '''TODO add sql command'''
        elif arglist[1]=="transactions":
            '''TODO add sql command'''
        else:
            print(arglist,"is not implemented")
            print_commands()
    elif arglist[0]=="add":
        if len(arglist)!= 2:
            print_commands()
        elif arglist[1]=="category":
            '''TODO add sql command'''
        elif arglist[1]=="transaction":
            '''TODO add sql command'''
        else:
            print(arglist,"is not implemented")
            print_commands()
    elif arglist[0]=="modify":
        if len(arglist)!= 2:
            print_commands()
        elif arglist[1]=="category":
            '''TODO add sql command'''
        else:
            print(arglist,"is not implemented")
            print_commands()
    elif arglist[0]=="delete":
        if len(arglist)!= 2:
            print_commands()
        elif arglist[1]=="transaction":
            '''TODO add sql command'''
        else:
            print(arglist,"is not implemented")
            print_commands()
    elif arglist[0]=="summarize":
        if len(arglist)!= 4:
            print_commands()
        if arglist[1]=="transactions" and arglist[2]=="by":
            if arglist[3]=="date":
                '''TODO add sql command'''
            elif arglist[3]=="month":
                '''TODO add sql command'''
            elif arglist[3]=="year":
                '''TODO add sql command'''
            elif arglist[3]=="category":
                '''TODO add sql command'''
            else:
                print(arglist,"is not implemented")
                print_commands()
        else:
            print(arglist,"is not implemented")
            print_commands()
    elif len(arglist) == 3 and arglist[0]=="print" and arglist[1]=="this" and arglist[2]=="menu":
        '''TODO add sql command'''
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

if len(sys.argv)==1:
    # they didn't pass any arguments, so prompt for them:
    print_usage()
    args = input("command> ").split(" ")
else:
    args = sys.argv[1:]
# now we can get process the arguments
process_args(args)

# and finally we commit our changes and close the connection
con.commit()
con.close()
"""