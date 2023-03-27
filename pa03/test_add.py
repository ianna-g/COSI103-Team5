from transaction import *

trans = Transaction("testsss")
sample_1 = { "amount": 45.0, "category": 1, "date": "2023-02-10", "description": "two tickets for cornmaze" }
sample_2 = { "amount": 55.0, "category": 2, "date": "2013-02-10", "description": "concert" }
sample_2_data = ( 1, 55.0, 2, "2013-02-10", "concert" )
sample_2_cate = ( 2, 'concert' )

def test_add_transaction():
    """ test add_transaction() """
    expected = [{ "item #": 1, "amount": 45.0, "category": 1, "date": "2023-02-10", "description": "two tickets for cornmaze"}]
    trans.add_transaction(sample_1)
    assert trans.show_transactions() == expected

def test_add_category():
    """ test add_category() """
    trans.add_category("technology")
    expected = [{ "id": 1, "name": "technology" }]
    assert trans.show_categories() == expected

def test_check_category_exists():
    """ test to see if category exists in category table """
    is_true = True
    is_false = False
    print(trans.show_categories)
    assert trans.check_category_exists("technology") == is_true
    assert trans.check_category_exists("pet products") == is_false

def test_toDictTransactions():
    expected = { "item #": 1, "amount": 55.0, "category": 2, "date": "2013-02-10", "description": "concert" }
    assert toDictTransactions(sample_2_data) == expected
    
def test_toDictCategories():
    expected = { "id": 2, "name": "concert" }
    assert toDictCategories(sample_2_cate) == expected