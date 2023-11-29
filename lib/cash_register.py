#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.discount = discount
        self.items = []

    def add_item(self, item, price, quantity=1):
        self.total += price * quantity
        self.items.extend([{"item": item, "price": price, "quantity": quantity}] * quantity)

    def apply_discount(self):
        if self.discount > 0:
            discount_decimal = self.discount / 100.0
            discount_amount = self.total * discount_decimal
            self.total -= discount_amount
            return f"After the discount, the total comes to ${self.total:.2f}."
        else:
            return "There is no discount to apply."

    def void_last_transaction(self):
        if self.items:
            last_transaction = self.items.pop()
            last_transaction_amount = last_transaction["price"] * last_transaction["quantity"]
            self.total -= last_transaction_amount
            return f"Last transaction voided: ${last_transaction_amount:.2f}"
        else:
            return "No transactions to void."
