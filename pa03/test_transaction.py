# test for each method in Transaction class
#Class written by Shaithea
import pytest
from transaction import *
# t_trans = Transaction("testdatabase123")
# print(t_trans.show_transactions())
# t_trans.add_transaction({ 'amount': 10, 'category': 1, 'date': '2023-03-25', 'description': 'testing123' })
# print(t_trans.show_transactions())

t = Transaction("testTransaction123")

# t.delete_transaction(1)

# ------------------- TESTS ------------------- #

t.add_category("Food")
# t.add_category("Technology")
t.add_transaction({ 'amount': 6.0, 'category': "Food", 'date': '2022-07-11', 'description': 'oreos' })
# t.add_transaction({ 'amount': 1000.0, 'category': "Technology", 'date': '2022-05-21', 'description': 'laptop' })

def test_modify_category():
    t.modify_category(1, "Snack")
    categories = t.get_category(1)
    expected = "Snack"
    assert categories == expected

def test_delete_transaction():
    t.delete_transaction(1)
    results = t.show_transactions()
    expected = []
    assert results == expected

