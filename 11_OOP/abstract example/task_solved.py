from abc import ABC, abstractmethod


class PaymentMethod(ABC):
    @abstractmethod
    def process_payment(self, amount: float) -> bool:
        pass

    @abstractmethod
    def refund_payment(self, amount: float) -> bool:
        pass


class CreditCardPayment(PaymentMethod):
    def process_payment(self, amount: float) -> bool:
        # Symulacja przetwarzania płatności kartą kredytową
        # Sprawdź poprawność danych karty, łącz się z bramką płatności, itp.
        print(f"Przetwarzanie płatności kartą kredytową dla kwoty {amount}...")
        # Symulacja zawsze pomyślnego przetworzenia płatności
        return True

    def refund_payment(self, amount: float) -> bool:
        # Symulacja zwrotu płatności kartą kredytową
        # Zwróć odpowiednią kwotę na kartę, zaktualizuj dane transakcji, itp.
        print(f"Zwrot płatności kartą kredytową dla kwoty {amount}...")
        # Symulacja zawsze pomyślnego zwrotu płatności
        return True


class PayPalPayment(PaymentMethod):
    def process_payment(self, amount: float) -> bool:
        # Symulacja przetwarzania płatności przez PayPal
        # Połącz się z serwisem PayPal, przekazując dane płatności, itp.
        print(f"Przetwarzanie płatności przez PayPal dla kwoty {amount}...")
        # Symulacja zawsze pomyślnego przetworzenia płatności
        return True

    def refund_payment(self, amount: float) -> bool:
        # Symulacja zwrotu płatności przez PayPal
        # Wywołaj odpowiednie metody API PayPal do zrealizowania zwrotu, itp.
        print(f"Zwrot płatności przez PayPal dla kwoty {amount}...")
        # Symulacja zawsze pomyślnego zwrotu płatności
        return True


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
