"""Orange Basket feature tests."""



# pytest-bdd generate features/oranges.feature > tests/acceptance/test_oranges_steps.py

from pytest_bdd import (

    given,

    scenarios,

    then,

    when,

    parsers

)



from project.oranges  import OrangeBasket



scenarios('../../feature/oranges.feature')
def test_add_oranges_to_a_basket():

    """Add oranges to a basket."""




@given(parsers.parse('the basket has {initial:d} oranges'),target_fixture='basket')

def the_basket_has_2_oranges(initial):

    """the basket has 2 oranges."""

    # raise NotImplementedError

    basket=OrangeBasket(initial_count=initial)

    return  basket



@when(parsers.parse('{more:d} oranges are added to the basket'))

def oranges_are_added_to_the_basket(basket, more):  # basket is the same as the basket in line 19
    """4 oranges are added to the basket."""
    basket.add(more)
    
@when(parsers.parse('{some:d} oranges are removed'))

def oranges_are_removed(basket,some):

    """4 oranges are added to the basket."""

    # raise NotImplementedError

    basket.remove(some)    




@then(parsers.parse('the basket contains {final:d} oranges'))

def the_basket_contains_6_oranges(basket,final):

    """the basket contains 6 oranges."""

    assert basket.count==final