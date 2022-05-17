"""Orange Basket feature tests."""

from pytest_bdd import (
    given,
    scenarios,
    then,
    when,
    parsers
)


from project.oranges import OrangeBasket # To make a basket.

scenarios("../../features/oranges.feature")
def test_oranges_to_a_basket():

    """Add or remove oranges to a basket."""



@given(parsers.parse('the basket has {initial:d} oranges'), target_fixture='basket') 
        # target_fixture gives variable name for the returned value of a function.

def the_basket_has_2_oranges(initial): 
    """the basket has 2 oranges."""
    basket = OrangeBasket(initial_count= initial) # Make a basket with 2 oranges.
    return basket


@when(parsers.parse('{more:d} oranges are added to the basket'))

def oranges_are_added_to_the_basket(basket, more):  # basket is the same as the basket in line 19
    """4 oranges are added to the basket."""
    basket.add(more)

@when(parsers.parse('{some:d} oranges are removed from the basket'))
def oranges_are_removed(basket, some): {
    basket.remove(some)
}


@then(parsers.parse('the basket contains {final:d} oranges'))
def the_basket_contains_6_oranges(basket, final):   # basket is the same as the basket in line 19
    """Check if the basket contains 6 oranges."""
    assert basket.count == final


# python -m test to run pytest