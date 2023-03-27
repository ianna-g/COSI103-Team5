Rose
^ I've added my name above any parts of the project I edited so that if anyone has questions about a part of the code they know who to ask.
We can keep this or get rid of it depending on if ppl think its helpful or not!

TODO add a desciption of our app and the following

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
