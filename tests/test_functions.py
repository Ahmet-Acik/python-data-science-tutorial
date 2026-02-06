import pytest

def add_numbers(a, b):
    """Simple function to add two numbers."""
    return a + b

def test_add_numbers():
    """Test basic addition."""
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0, 0) == 0

def test_add_numbers_types():
    """Test addition with different types."""
    assert add_numbers(2.5, 3.5) == 6.0
    assert add_numbers("hello", "world") == "helloworld"

if __name__ == "__main__":
    pytest.main([__file__])