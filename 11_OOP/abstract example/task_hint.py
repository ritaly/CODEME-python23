from abc import ABC, abstractmethod


#Utwórz klasę abstrakcyjną
class PaymentMethod():
    pass


class CreditCardPayment(PaymentMethod):
    def process_payment(self, amount: float) -> bool:
        pass

    def refund_payment(self, amount: float) -> bool:
        pass


class PayPalPayment(PaymentMethod):
    def process_payment(self, amount: float) -> bool:
        pass

    def refund_payment(self, amount: float) -> bool:
        pass


def main():
    # Tworzenie instancji płatności
    credit_card_payment = CreditCardPayment()
    paypal_payment = PayPalPayment()

    # Testowanie systemu płatności
    payment_amount = 100.0

    # Przetwarzanie płatności
    if credit_card_payment.process_payment(payment_amount):
        print("Płatność kartą kredytową została pomyślnie przetworzona.")
    else:
        print("Przetwarzanie płatności kartą kredytową nie powiodło się.")

    if paypal_payment.process_payment(payment_amount):
        print("Płatność przez PayPal została pomyślnie przetworzona.")
    else:
        print("Przetwarzanie płatności przez PayPal nie powiodło się.")

    # Zwrot płatności
    refund_amount = 50.0

    if credit_card_payment.refund_payment(refund_amount):
        print("Zwrot płatności kartą kredytową został pomyślnie zrealizowany.")
    else:
        print("Zwrot płatności kartą kredytową nie powiódł się.")

    if paypal_payment.refund_payment(refund_amount):
        print("Zwrot płatności przez PayPal został pomyślnie zrealizowany.")
    else:
        print("Zwrot płatności przez PayPal nie powiódł się.")


if __name__ == '__main__':
    main()