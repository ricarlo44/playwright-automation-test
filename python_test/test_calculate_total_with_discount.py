from python_test.main import calculate_order_total

class TesteCalculateTotalWithDiscount:

    def test_single_item_with_discount(self, single_item):
       # items = [{'price': 50.0, 'quantity': 1}]
        result = calculate_order_total(single_item, apply_discount=True)
        assert result == 45.0  # Assuming a 10% discount

    def test_multiple_items_with_discount(self, multiple_items):
      #  items = [
       #     {'price': 50.0, 'quantity': 1},
       #     {'price': 25.0, 'quantity': 2}
       # ]
        result = calculate_order_total(multiple_items, apply_discount=True)
        assert result == 90.0  # Assuming a 10% discount