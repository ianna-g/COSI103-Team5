import pytest
from transaction import *

# Be sure to delete the abc123 and 123abc file at your home directory or this will fail since it needs a new file every time

def test_show_transaction():
    # Test that show_transaction works when adding entries
    t_trans = Transaction("abc123")
    expected = "[]"
    assert t_trans.show_transactions().__str__() == expected
    t_trans.add_transaction({ 'amount': 10, 'category': 1, 'date': '2023-03-25', 'description': 'testing123' })
    expected = "[{'item #': 1, 'amount': 10.0, 'category': 1, 'date': '2023-03-25', 'description': 'testing123'}]"
    assert t_trans.show_transactions().__str__() == expected
    t_trans.add_transaction({ 'amount': 1, 'category': 2, 'date': '2023-04-20', 'description': 'testingABC' })
    expected = "[{'item #': 1, 'amount': 10.0, 'category': 1, 'date': '2023-03-25', 'description': 'testing123'}, {'item #': 2, 'amount': 1.0, 'category': 2, 'date': '2023-04-20', 'description': 'testingABC'}]"
    # TODO Test that show_transaction works when removing entries

def test_show_catagories():
    t_trans = Transaction("123abc")
    expected = "[]"
    assert t_trans.show_categories().__str__() == expected
    t_trans.add_category("ONE")
    expected = "[{'id': 1, 'name': 'ONE'}]"
    assert t_trans.show_categories().__str__() == expected
    t_trans.add_category("TWO")
    expected = "[{'id': 1, 'name': 'ONE'}, {'id': 2, 'name': 'TWO'}]"
    assert t_trans.show_categories().__str__() == expected
    # TODO Test that show_catagories works when modifying entries