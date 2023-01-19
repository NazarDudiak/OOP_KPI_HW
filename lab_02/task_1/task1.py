import random
import string


class Ticket:
    """
    All tickets must have the following properties:

    - the ability to construct a ticket by number;
    - the ability to ask for a ticket’s price;
    - the ability to print a ticket as a String.
    """
    _regular_price = 10
    _advance_ticket = _regular_price * 0.6
    _student_ticket = _regular_price * 0.5
    _late_ticket = _regular_price * 1.10

    def generate_unique_number(self, number_length=9, symbols_type=None):
        """
        :param number_length: length of unique number which will generate
        :param symbols_type: [0] = lower, [1] = upper, [2] = num, [3] = symbols
        :return: generated unique number
        """
        if symbols_type is None:
            symbols_type = [1, 1, 1, 0]
        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        num = string.digits
        symbols = string.punctuation
        all_symbols = ""

        if symbols_type[0] == 1:
            all_symbols += lower
        if symbols_type[1] == 1:
            all_symbols += upper
        if symbols_type[2] == 1:
            all_symbols += num
        if symbols_type[3] == 1:
            all_symbols += symbols

        temp = random.sample(all_symbols * 5, number_length)
        self.unique_number = "".join(temp)
        return self.unique_number

    def __init__(self, unique_number=None):
        if unique_number:
            self.unique_number = unique_number
        else:
            self.unique_number = self.generate_unique_number()

        print("Tickets types:\n\t[1] - Regular ticket")
        print("\t[2] - advance ticket (purchased 60 or more days before the event)")
        print("\t[3] - Late ticket (purchased fewer than 10 days before the event)")
        print("\t[4] - Student ticket (50% of Regular ticket.")
        ticket_type = None
        while ticket_type not in ["1", "2", "3", "4"]:
            ticket_type = input("Enter type of the ticket:")
            if ticket_type == "1":
                self.ticket_price = self._regular_price
            elif ticket_type == "2":
                self.ticket_price = self._advance_ticket
            elif ticket_type == "3":
                self.ticket_price = self._late_ticket
            elif ticket_type == "4":
                self.ticket_price = self._student_ticket
            elif ticket_type == "exit":
                break
            else:
                print("Error! ", end="")

    def __str__(self):
        return f"""\nYour Ticket:
        ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
        ░░░░░░██████████████████████████████████████████░░░░░░
        ░░░░░░██░░░░Ticket░░░░░░░░░░░░░░░░░KPI_Event░░██░░░░░░
        ░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░░░░░░
        ░░░░░░██░░░░Price░░░░░░░░░░░░░░░░░░{self.ticket_price:░<4}░░░░░░░██░░░░░░
        ░░░░░░██░░░░Ticket No.░░░░░░░░░░░░░{self.unique_number:░<10}░██░░░░░░
        ░░░░░░██████████████████████████████████████████░░░░░░
        ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░"""

    def get_price(self):
        return self.ticket_price


print("Example 1")
example = Ticket()
print(example.get_price())
print(example)

print("\n\nExample 2")
example_01 = Ticket("1234567890")
print(example_01.get_price())
print(example_01)
