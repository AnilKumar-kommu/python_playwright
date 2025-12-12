
#assertions
def test_assertions():
    # Test equality
    assert 2 + 2 == 4, "Addition failed"

    # Test inequality
    assert 5 - 3 != 1, "Subtraction failed"

    # Test membership
    assert 'a' in 'apple', "'a' should be in 'apple'"

    # Test type
    assert isinstance(3.14, float), "3.14 should be a float"

    # Test truthiness
    assert True, "This should be true"

    print("All assertions passed!")
test_assertions()
