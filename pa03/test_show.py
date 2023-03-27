"""tests that the show_transaction() and show_categories() methods work"""
import transaction

# Be sure to delete the abc123 and 123abc file at your home directory
# or this will fail since it needs a new file every time
# Author: Rose


def test_show_transaction():
    """tests that the show_transaction() method works"""
    # Test that show_transaction works when adding entries
    t_trans = transaction.Transaction("abc123")
    expected = "[]"
    assert str(t_trans.show_transactions()) == expected
    t_trans.add_transaction({ 'amount': 10, 'category': 1,
                             'date': '2023-03-25', 'description': 'testing123' })
    expected = """[{'item #': 1, 'amount': 10.0, 'category': 1,'date': '2023-03-25',
    'description': 'testing123'}]"""
    assert str(t_trans.show_transactions()) == expected
    t_trans.add_transaction({ 'amount': 1, 'category': 2, 'date': '2023-04-20',
                             'description': 'testingABC' })
    expected = """[{'item #': 1, 'amount': 10.0, 'category': 1, 'date': '2023-03-25',
    'description': 'testing123'}, {'item #': 2, 'amount': 1.0, 'category': 2,
    'date': '2023-04-20', 'description': 'testingABC'}]"""
    # Test that show_transaction works when removing entries
    t_trans.delete_transaction(2)
    expected = """[{'item #': 1, 'amount': 10.0, 'category': 1, 'date': '2023-03-25',
    'description': 'testing123'}]"""
    assert str(t_trans.show_transactions()) == expected
    t_trans.delete_transaction(1)
    expected = "[]"
    assert str(t_trans.show_transactions()) == expected

def test_show_categories():
    """tests that show_categories() works"""
    # Test that show_catagories works when adding entries
    t_trans = transaction.Transaction("123abc")
    expected = "[]"
    assert str(t_trans.show_categories()) == expected
    t_trans.add_category("ONE")
    expected = "[{'id': 1, 'name': 'ONE'}]"
    assert str(t_trans.show_categories()) == expected
    t_trans.add_category("TWO")
    expected = "[{'id': 1, 'name': 'ONE'}, {'id': 2, 'name': 'TWO'}]"
    assert str(t_trans.show_categories()) == expected
    # Test that show_catagories works when modifying entries
    t_trans.modify_category(1, "NEW")
    expected = "[{'id': 1, 'name': 'NEW'}, {'id': 2, 'name': 'TWO'}]"
    assert str(t_trans.show_categories()) == expected
    