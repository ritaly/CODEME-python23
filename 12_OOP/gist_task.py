# rozwiązanie do zadania dla chetnych
# https://gist.github.com/ritaly/6b2a657f863aa50dc8a317b6e1d32170

import re
import csv


class Customer:

    def __init__(self, name: str, email: str):
        self.__name = name
        self.__email = email

    @property  # getter - zwraca wartość
    def name(self) -> str:
        return self.__name

    @name.setter  # setter - ustawia i nic nie zwraca
    def name(self, value: str) -> None:
        if not value:
            raise ValueError("Name cannot be empty")
        self.__name = value

    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, value: str) -> None:
        if not self.__validate_email(value):
            raise ValueError("Invalid email format")

        self.__email = value

    @staticmethod
    def __validate_email(email: str) -> bool:  # waliduje email z użyciem regular expression
        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return bool(re.match(pattern, email))

    def save_to_csv(self, filename: str) -> None:
        data = {"Name": self.__name, "Email": self.__email}

        try:
            with open(filename, "w", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=data.keys())
                writer.writeheader()
                writer.writerow(data)
            print(f"Customer data saved to {filename} successfully.")

        except Exception as err:
            print(f"Error saving customer data to {filename}: {str(err)}")


def main():
    customer = Customer("John Doe", "john.doe@example.com")

    print(customer.name)  # Output: John Doe
    print(customer.email)  # Output: john.doe@example.com

    customer.name = "Jane Smith"
    customer.email = "jane.smith@example.com"
    customer.save_to_csv("customer_data.csv")

if __name__ == "__main__":
    main()