import pytest
from python_test.main import calculate_order_total


class TestEmptyList:
    def test_empty_list_raise_error(self):
        with pytest.raises(ValueError, match="Items list cannot be empty"):
            calculate_order_total([])
    def test_none_raise_error(self):
        with pytest.raises(ValueError, match="Items list cannot be empty"):
            calculate_order_total(None)