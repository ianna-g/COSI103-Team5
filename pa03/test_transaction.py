#tests for modify_category and delete_transaction methods
#Class written by Shaithea

"""imports"""
from transaction import *

t = Transaction("testTransaction123")
t.add_category("Food")
t.add_transaction({ 'amount': 6.0, 'category': "Food",
'date': '2022-07-11', 'description': 'oreos' })

def test_modify_category():
    """ Test for modify_category method """
    t.modify_category(1, "Snack")
    categories = t.get_category(1)
    expected = "Snack"
    assert categories == expected
    
def test_delete_transaction():
    """ Test for delete_transaction method """
    t.delete_transaction(1)
    results = t.show_transactions()
    expected = []
    assert results == expected
