## Zadanie: System płatności w sklepie internetowym

Twoim zadaniem jest stworzenie systemu płatności dla sklepu internetowego. Aby to osiągnąć, musisz wykorzystać klasę abstrakcyjną do zaimplementowania ogólnych metod i zachowań, które będą wspólne dla wszystkich metod płatności, ale będą różnić się szczegółami w zależności od konkretnej metody płatności.

### Wymagania:

1. Stwórz klasę abstrakcyjną o nazwie "PaymentMethod", która będzie zawierać następujące metody abstrakcyjne:

   - `process_payment(amount: float) -> bool`:

   - `refund_payment(amount: float) -> bool`:

2. Stwórz co najmniej dwie klasy dziedziczące po klasie abstrakcyjnej "PaymentMethod", które będą reprezentować różne metody płatności.

3. Dla każdej z klas dziedziczących:

   - Zaimplementuj metodę `process_payment(amount: float) -> bool` w taki sposób, aby symulować przetwarzanie płatności za pomocą konkretnej metody płatności.

   - Zaimplementuj metodę `refund_payment(amount: float) -> bool` w taki sposób, aby symulować zwrot płatności za pomocą konkretnej metody płatności.

4. Stwórz instancje obu klas płatności.

5. Przetestuj działanie systemu płatności, wykonując następujące kroki:

   - Wywołaj metodę `process_payment(amount: float) -> bool` dla obu instancji, przekazując kwotę do zapłaty. Sprawdź, czy płatność została pomyślnie przetworzona i wyświetl odpowiedni komunikat.

   - Wywołaj metodę `refund_payment(amount: float) -> bool` dla obu instancji, przekazując kwotę do zwrotu. Sprawdź, czy zwrot został pomyślnie przetworzony i wyświetl odpowiedni komunikat.

Uwaga: Nie jest wymagane implementowanie pełnego systemu sklepu internetowego. Skup się tylko na implementacji klas abstrakcyjnych, dziedziczących klas płatności i przetestowaniu ich funkcjonalności.
