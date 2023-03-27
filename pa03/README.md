# App Description
This app creates a database to keep track of transactions. Run the tracker.py file to start the app. Your database data is stored in a file at the provided HOME directory, and so your data will be saved in between runs of this application. Each file will have a unique database so you can use this app to keep multiple transaction databases!
This app lets you add categories and modify (rename) them. You can also add transactions, which each have an amount, category, date, and description. You can delete any transaction by entering it's unique ID. Finally, you can summarize the transactions in any file's database by their category, date, year, or month. The summary will provide the number of transactions in each group, and the sum of the amounts.


# TODO add the following
- a script of you running pylint, and
- then running pytest, and
- then running tracker.py and demonstrating all of the features you added

Creating a transcript -
create a transcript of your session as you demonstrate each of the features you have implemented.
create a README.md file which describes your app and contains

- a script of you running pylint, and
- then running pytest, and
- then running tracker.py and demonstrating all of the features you added

# Work Allocation

Ianna: summarize
Minsung: add
Rose: show
Anusha: modify/delete

# Pytest Transcript

## Show Transaction and Show Category Operations

- Testing show_transaction() and show_category()

```
rootdir: C:\Users\arose\Documents\GitHub\COSI103-Team5
plugins: anyio-3.6.2
collected 2 items                                                                                                                                               

pa03\test_show.py ..                                                                                                                                     [100%] 

====================================================================== 2 passed in 0.35s ====================================================================== 
PS C:\Users\arose\Documents\GitHub\COSI103-Team5>
```

## Add Transaction and Add Category Operations

- Testing add_transaction(), add_category(), check_category_exists(), toDictTransactions(), and toDictCategories()

```
(base) minsungs-mac:pa03 minsungkim$ pytest test_add.py
============================================================================================== test session starts ==============================================================================================
platform darwin -- Python 3.9.7, pytest-6.2.4, py-1.10.0, pluggy-0.13.1
rootdir: /Users/minsungkim/Coding/COSI103/Team5/pa03
plugins: anyio-2.2.0
collected 5 items

test_add.py .....                                                                                                                                                                                         [100%]

=============================================================================================== 5 passed in 0.17s ===============================================================================================
```

## Summary by Date, Month, Year and Categoty Operations
```
(base) iannag@iannas-air pa03 % pytest test_summary.py
================================================================= test session starts =================================================================
platform darwin -- Python 3.11.1, pytest-7.2.1, pluggy-1.0.0
rootdir: /Users/iannag/Desktop/Git-Hub/COSI103-Team5/pa03
collected 4 items                                                                                                                                     

test_summary.py ....                                                                                                                            [100%]

================================================================== 4 passed in 0.01s ==================================================================
```

# tracker.py Demonstration Transcript

## Add Transaction and Add Category Operations

- Demonstration of add category, add transaction, show categories, and show transactions

```
Enter filename of database you would like to interact with (omit the .db extension): Finance
[]

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

Enter Option # (11 to view options) > 2
Add Category
Categories
[]
no categories to print
Enter new category:
> technology

New Category Saved!

Enter Option # (11 to view options) > 5
Add Transaction
Select category index for transaction (or -1 to cancel):
[(1, 'TECHNOLOGY')]

index                name
----------------------------------------
1                    TECHNOLOGY
----------------------------------------

> 1
Enter transaction details (amount;date(YYYY-MM-DD);description):
> 45.0; 2023-03-20; iphone charger

Transaction Entry Successful!

Enter Option # (11 to view options) > 1
Show Categories
[(1, 'TECHNOLOGY')]

index                name
----------------------------------------
1                    TECHNOLOGY
----------------------------------------

Enter Option # (11 to view options) > 4
Transactions

item #     amount     category        date            description
--------------------------------------------------------------------------------
1          45.0       TECHNOLOGY      2023-03-20      iphone charger
--------------------------------------------------------------------------------

Enter Option # (11 to view options) > 0
```


## Show Transaction and Show Categories Operations

```
PS C:\Users\arose\Documents\GitHub\COSI103-Team5> python pa03/tracker.py  
Enter filename of database you would like to interact with (omit the .db extension): testy

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
    
Enter Option # (11 to view options) > 1
Show Categories

index                name
----------------------------------------
1                    NEWNAME
2                    MECH
3                    BEEF
4                    LILAC
5                    POKEMON
----------------------------------------

Enter Option # (11 to view options) > 4
Transactions

item #     amount     category        date            description
--------------------------------------------------------------------------------
1          100.5      MECH            2003-01-01      huge mech bodysuit
2          2.0        NEWNAME         2020-04-23      computer
5          15.0       POKEMON         2017-10-17      enlighteningly harrowing
--------------------------------------------------------------------------------

Enter Option # (11 to view options) >
```
