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
Shaithea: modify/delete

# Pylint Transcript

- Pylint for tracker.py

(base) shaithea@Shaitheas-MacBook-Pro pa03 % pylint tracker.py
************* Module tracker
tracker.py:139:0: C0325: Unnecessary parens after 'if' keyword (superfluous-parens)
tracker.py:159:0: C0325: Unnecessary parens after 'if' keyword (superfluous-parens)
tracker.py:196:69: C0303: Trailing whitespace (trailing-whitespace)
tracker.py:265:0: C0301: Line too long (123/100) (line-too-long)
tracker.py:5:0: W0401: Wildcard import transaction (wildcard-import)
tracker.py:267:0: C0103: Constant name "interface_active" doesn't conform to UPPER_CASE naming style (invalid-name)
tracker.py:279:16: C0103: Constant name "interface_active" doesn't conform to UPPER_CASE naming style (invalid-name)
tracker.py:5:0: W0614: Unused import sqlite3 from wildcard import (unused-wildcard-import)
tracker.py:5:0: W0614: Unused import os from wildcard import (unused-wildcard-import)
tracker.py:5:0: W0614: Unused import toDictTransactions from wildcard import (unused-wildcard-import)
tracker.py:5:0: W0614: Unused import toDictCategories from wildcard import (unused-wildcard-import)
tracker.py:5:0: W0614: Unused import toDictSumByDate from wildcard import (unused-wildcard-import)
tracker.py:5:0: W0614: Unused import toDictSumByMonth from wildcard import (unused-wildcard-import)
tracker.py:5:0: W0614: Unused import toDictSumByYear from wildcard import (unused-wildcard-import)
tracker.py:5:0: W0614: Unused import toDictSumByCategory from wildcard import (unused-wildcard-import)
tracker.py:6:0: C0411: standard import "import datetime" should be placed before "from transaction import *" (wrong-import-order)

------------------------------------------------------------------
Your code has been rated at 9.32/10 (previous run: 9.32/10, +0.00)

- Pylint for transaction.py

(base) shaithea@Shaitheas-MacBook-Pro pa03 % pylint transaction.py
************* Module transaction
transaction.py:55:0: C0303: Trailing whitespace (trailing-whitespace)
transaction.py:78:0: C0303: Trailing whitespace (trailing-whitespace)
transaction.py:90:0: C0303: Trailing whitespace (trailing-whitespace)
transaction.py:103:0: C0303: Trailing whitespace (trailing-whitespace)
transaction.py:116:0: C0303: Trailing whitespace (trailing-whitespace)
transaction.py:129:0: C0303: Trailing whitespace (trailing-whitespace)
transaction.py:133:0: C0301: Line too long (194/100) (line-too-long)
transaction.py:134:0: C0303: Trailing whitespace (trailing-whitespace)
transaction.py:146:56: C0303: Trailing whitespace (trailing-whitespace)
transaction.py:149:0: C0303: Trailing whitespace (trailing-whitespace)
transaction.py:159:0: C0303: Trailing whitespace (trailing-whitespace)
transaction.py:163:0: C0303: Trailing whitespace (trailing-whitespace)
transaction.py:183:0: C0301: Line too long (127/100) (line-too-long)
transaction.py:184:0: C0303: Trailing whitespace (trailing-whitespace)
transaction.py:185:23: C0303: Trailing whitespace (trailing-whitespace)
transaction.py:188:0: C0301: Line too long (154/100) (line-too-long)
transaction.py:189:0: C0303: Trailing whitespace (trailing-whitespace)
transaction.py:190:22: C0303: Trailing whitespace (trailing-whitespace)
transaction.py:193:0: C0301: Line too long (151/100) (line-too-long)
transaction.py:194:0: C0303: Trailing whitespace (trailing-whitespace)
transaction.py:198:0: C0301: Line too long (135/100) (line-too-long)
transaction.py:5:0: C0103: Function name "toDictTransactions" doesn't conform to snake_case naming style (invalid-name)
transaction.py:5:0: C0103: Argument name "t" doesn't conform to snake_case naming style (invalid-name)
transaction.py:11:0: C0103: Function name "toDictCategories" doesn't conform to snake_case naming style (invalid-name)
transaction.py:11:0: C0103: Argument name "c" doesn't conform to snake_case naming style (invalid-name)
transaction.py:17:0: C0103: Function name "toDictSumByDate" doesn't conform to snake_case naming style (invalid-name)
transaction.py:17:0: C0103: Argument name "t" doesn't conform to snake_case naming style (invalid-name)
transaction.py:24:0: C0103: Function name "toDictSumByMonth" doesn't conform to snake_case naming style (invalid-name)
transaction.py:24:0: C0103: Argument name "t" doesn't conform to snake_case naming style (invalid-name)
transaction.py:31:0: C0103: Function name "toDictSumByYear" doesn't conform to snake_case naming style (invalid-name)
transaction.py:31:0: C0103: Argument name "t" doesn't conform to snake_case naming style (invalid-name)
transaction.py:38:0: C0103: Function name "toDictSumByCategory" doesn't conform to snake_case naming style (invalid-name)
transaction.py:38:0: C0103: Argument name "t" doesn't conform to snake_case naming style (invalid-name)
transaction.py:46:4: W0105: String statement has no effect (pointless-string-statement)
transaction.py:58:38: W0622: Redefining built-in 'tuple' (redefined-builtin)
transaction.py:58:4: C0103: Method name "runCategoryQuery" doesn't conform to snake_case naming style (invalid-name)
transaction.py:69:28: W0622: Redefining built-in 'tuple' (redefined-builtin)
transaction.py:69:4: C0103: Method name "runQuery" doesn't conform to snake_case naming style (invalid-name)
transaction.py:81:37: W0622: Redefining built-in 'tuple' (redefined-builtin)
transaction.py:81:4: C0103: Method name "runQuerySumByDate" doesn't conform to snake_case naming style (invalid-name)
transaction.py:93:38: W0622: Redefining built-in 'tuple' (redefined-builtin)
transaction.py:93:4: C0103: Method name "runQuerySumByMonth" doesn't conform to snake_case naming style (invalid-name)
transaction.py:106:37: W0622: Redefining built-in 'tuple' (redefined-builtin)
transaction.py:106:4: C0103: Method name "runQuerySumByYear" doesn't conform to snake_case naming style (invalid-name)
transaction.py:119:41: W0622: Redefining built-in 'tuple' (redefined-builtin)
transaction.py:119:4: C0103: Method name "runQuerySumByCategory" doesn't conform to snake_case naming style (invalid-name)
transaction.py:208:4: C0103: Argument name "newName" doesn't conform to snake_case naming style (invalid-name)

------------------------------------------------------------------
Your code has been rated at 5.91/10 (previous run: 5.91/10, +0.00)

- Pylint for test_treansaction.py

(base) shaithea@Shaitheas-MacBook-Pro pa03 % pylint test_transaction.py

---------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: -6.43/10, +16.43)

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

- Testing sum_by_date(), sum_by_month(), sum_by_year(), and sum_by_category()

```
(base) iannag@iannas-air pa03 % pytest test_summary.py
================================================================= test session starts =================================================================
platform darwin -- Python 3.11.1, pytest-7.2.1, pluggy-1.0.0
rootdir: /Users/iannag/Desktop/Git-Hub/COSI103-Team5/pa03
collected 4 items                                                                                                                                     

test_summary.py ....                                                                                                                            [100%]

================================================================== 4 passed in 0.01s ==================================================================
```

## Modify and Delete Operations

- Testing modify_category() and delete_transaction()

(base) shaithea@Shaitheas-MacBook-Pro pa03 % pytest test_transaction.py
========================================================= test session starts ==========================================================
platform darwin -- Python 3.9.7, pytest-6.2.4, py-1.10.0, pluggy-0.13.1
rootdir: /Users/shaithea/Documents/GitHub/COSI103-Team5/pa03
plugins: anyio-2.2.0
collected 2 items                                                                                                                      

test_transaction.py ..                                                                                                           [100%]

========================================================== 2 passed in 0.02s ===========================================================

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

## Summary Operations
(base) iannag@iannas-air pa03 % python3 tracker.py
Enter filename of database you would like to interact with (omit the .db extension): FinanceTracker.db

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
    
Enter Option # (11 to view options) > 4
Transactions

item #     amount     category        date            description    
--------------------------------------------------------------------------------
1          30.0       5               2010-03-01      picnic         
2          50.0       5               2010-03-01      outing         
3          4.0        1               2023-05-25      snacks         
--------------------------------------------------------------------------------

Enter Option # (11 to view options) > 7
summarize transactions by date

date          category   # of transactions    sum of transaction amounts
---------------------------------------------------------------------------
2010-03-01    5          2                    80.0                
2023-05-25    1          1                    4.0                 
---------------------------------------------------------------------------

Enter Option # (11 to view options) > 8
summarize transactions by month
[{'month': '03', 'category': 1, '# of transactions': 2, 'sum of transaction amounts': 80.0}, {'month': '05', 'category': 2, '# of transactions': 1, 'sum of transaction amounts': 4.0}]

month         category   # of transactions    sum of transaction amounts
---------------------------------------------------------------------------
03            5          2                    80.0                
05            1          1                    4.0                 
---------------------------------------------------------------------------

Enter Option # (11 to view options) > 9
summarize transactions by year
[{'year': '2010', 'category': 1, '# of transactions': 2, 'sum of transaction amounts': 80.0}, {'year': '2023', 'category': 2, '# of transactions': 1, 'sum of transaction amounts': 4.0}]

year          category   # of transactions    sum of transaction amounts
---------------------------------------------------------------------------
2010          5          2                    80.0                
2023          1          1                    4.0                 
---------------------------------------------------------------------------

Enter Option # (11 to view options) > 10
summarize transactions by category
[{'category': 1, 'date': '2010-03-01', '# of transactions': 2, 'sum of transaction amounts': 80.0}, {'category': 2, 'date': '2023-05-25', '# of transactions': 1, 'sum of transaction amounts': 4.0}]

category   date            # of transactions    sum of transaction amounts    
--------------------------------------------------------------------------------
5          2010-03-01      2                    80.0                          
1          2023-05-25      1                    4.0                           
--------------------------------------------------------------------------------
## Modify and Delete Categories Operations

(base) shaithea@Shaitheas-MacBook-Pro pa03 % python create_db.py
(base) shaithea@Shaitheas-MacBook-Pro pa03 % python tracker.py  
Enter filename of database you would like to interact with (omit the .db extension): FinanceTracker 

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
no categories to print
Enter Option # (11 to view options) > 2
Add Category
Categories
no categories to print
Enter new category:
> Food

New Category Saved!

Enter Option # (11 to view options) > 2
Add Category
Categories

index                name                
----------------------------------------
1                    FOOD                
----------------------------------------

Enter new category:
> Technology

New Category Saved!

Enter Option # (11 to view options) > 5
Add Transaction
Select category index (or -1 to cancel): 

index                name                
----------------------------------------
1                    FOOD                
2                    TECHNOLOGY          
----------------------------------------

> 1
Enter transaction details (amount;date(YYYY-MM-DD);description):
> 5;2023-03-02;oreo thins

Transaction Entry Successful!

Enter Option # (11 to view options) > 5
Add Transaction
Select category index (or -1 to cancel): 

index                name                
----------------------------------------
1                    FOOD                
2                    TECHNOLOGY          
----------------------------------------

> 2
Enter transaction details (amount;date(YYYY-MM-DD);description):
> 1000;2023-05-11;new laptop

Transaction Entry Successful!

Enter Option # (11 to view options) > 4
Transactions

item #     amount     category        date            description    
--------------------------------------------------------------------------------
1          5.0        FOOD            2023-03-02      oreo thins     
2          1000.0     TECHNOLOGY      2023-05-11      new laptop     
--------------------------------------------------------------------------------

Enter Option # (11 to view options) > 3
Modify Category
Categories

index                name                
----------------------------------------
1                    FOOD                
2                    TECHNOLOGY          
----------------------------------------

Select category index (or -1 to cancel): 

index                name                
----------------------------------------
1                    FOOD                
2                    TECHNOLOGY          
----------------------------------------

> 1
Enter new category name:
> snacks

Category Modified!

Enter Option # (11 to view options) > 1
Show Categories

index                name                
----------------------------------------
1                    SNACKS              
2                    TECHNOLOGY          
----------------------------------------

Enter Option # (11 to view options) > 4
Transactions

item #     amount     category        date            description    
--------------------------------------------------------------------------------
1          5.0        SNACKS          2023-03-02      oreo thins     
2          1000.0     TECHNOLOGY      2023-05-11      new laptop     
--------------------------------------------------------------------------------

Enter Option # (11 to view options) > 6
Delete Transaction
Select transaction index to delete (or -1 to cancel): 

item #     amount     category        date            description    
--------------------------------------------------------------------------------
1          5.0        SNACKS          2023-03-02      oreo thins     
2          1000.0     TECHNOLOGY      2023-05-11      new laptop     
--------------------------------------------------------------------------------

> 1

Transaction deleted.

Enter Option # (11 to view options) > 4
Transactions

item #     amount     category        date            description    
--------------------------------------------------------------------------------
2          1000.0     TECHNOLOGY      2023-05-11      new laptop     
--------------------------------------------------------------------------------
