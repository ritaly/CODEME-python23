 # Stwórz własną implementację kolejki FIFO.
 # Klasa kolejka (Queue) powinna na starcie przyjmować listę elementów.
 # Wśród metod powinny się znaleźć takie jak: wyswietlenie kolejki,
 # sprawdzenie czy jest pusta, dodanie elementu do kolejki (put), wyjęcie elementu z kolejki (get).

class Queue:
     def __init__(self, lst):
        self.lst = lst

     def show(self):
        print(self.lst)

     def is_empty(self):
        return len(self.lst) == 0

     def put(self, elem):
         self.lst.append(elem)
         print(f'Dodano element {elem} do kolejki')

     def get(self):
         return self.lst.pop(0)


def main():
    kolejka = Queue([4, 5, 7, 8, 12])
    kolejka.show()
    print(kolejka.is_empty())
    kolejka.put(6)
    print(kolejka.get())
    kolejka.show()


if __name__ == '__main__':
    main()