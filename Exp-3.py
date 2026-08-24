# Experiment 3
# Title: Design Patterns in Python

from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        card = input("Enter Credit Card Number: ")
        print("Card:", card)
        print(f"Payment of ${amount} paid successfully using Credit Card.")


class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        paypal_id = input("Enter PayPal ID: ")
        print("PayPal ID:", paypal_id)
        print(f"Payment of ${amount} paid successfully using PayPal.")


class BitcoinPayment(PaymentStrategy):
    def pay(self, amount):
        wallet = input("Enter Bitcoin Wallet Address: ")
        print("Wallet:", wallet)
        print(f"Payment of ${amount} paid successfully using Bitcoin.")

class PaymentProcessor:
    def __init__(self):
        self.strategy = None

    def set_strategy(self, strategy):
        self.strategy = strategy

    def process_payment(self, amount):
        if self.strategy is None:
            print("No payment method selected.")
        else:
            self.strategy.pay(amount)

processor = PaymentProcessor()

while True:
    print("\n1. Credit Card")
    print("2. PayPal")
    print("3. Bitcoin")
    print("4. Exit")

    choice = int(input("Select Payment Method: "))

    if choice == 4:
        print("Thank You!")
        break

    amount = float(input("Enter Payment Amount ($): "))

    if choice == 1:
        processor.set_strategy(CreditCardPayment())
    elif choice == 2:
        processor.set_strategy(PayPalPayment())
    elif choice == 3:
        processor.set_strategy(BitcoinPayment())
    else:
        print("Invalid Choice!")
        continue

    processor.process_payment(amount)
