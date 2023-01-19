import datetime


class Calendar:
    """
    Create a class CALENDAR. Define methods for creating and working with a CALENDAR instances and overload operations^
    "+=, -=" - for adding and subtracting days, months, years to a given date
    "==, ! =, >, >=, <, <=" - for comparing dates.
    """

    def __init__(self, start_date=datetime.date.today()):
        self.date = start_date
        self.month_final = None

    def add_to_date(self, days=0, months=0, years=0):
        if (self.date.month + (months % 12)) % 12 != 0:
            self.month_final = (self.date.month + (months % 12)) % 12
        else:
            self.month_final = 12

        start_day = self.date.day
        start_year = self.date.year

        while (self.date.month != self.month_final) or (self.date.year != (start_year + years)):
            self.date += datetime.timedelta(days=1)

        for i in range(start_day+days-1):
            self.date += datetime.timedelta(days=1)

        return self.date

    def subtract_from_date(self, days=0, months=0, years=0):
        start_day = self.date.day
        start_year = self.date.year

        if self.date.month - months > 0:
            self.month_final = self.date.month - months
        else:
            self.month_final = 12 - abs((self.date.month - months))

        while (self.date.month != self.month_final) or (self.date.year != (start_year - years)):
            self.date -= datetime.timedelta(days=1)

        last_month_day = self.date.day

        self.date -= datetime.timedelta(days=last_month_day-start_day+days)

        return self.date


def main():
    choose = input("Choose today's date or a given one?\n\t1. Today [T/t]\n\t2. Given one [G/g]\nAnswer: ").lower()
    if choose in ["t", "g", "1", "2"]:
        if choose in ["t", "1"]:
            test = Calendar()
            print("Today", test.date)
        elif choose in ["g", "2"]:
            day = input("Enter day: ")
            month = input("Enter month: ")
            year = input("Enter year: ")
            datetime.datetime.strptime(day + "/" + month + "/" + year, "%d/%m/%Y").date()

            test = Calendar()
            print("Your date:", test.date)
        else:
            test = Calendar()

        ans = get_date()
        option_day = int(ans[1])
        option_month = int(ans[2])
        option_year = int(ans[3])
        if ans[0] == 1:
            print(f"After {option_day} day(s), {option_month} month(s), {option_year} year(s) will be:",
                  test.add_to_date(days=option_day, months=option_month, years=option_year))
            # test.subtract_from_date(days=1, months=2, years=4)
        elif ans[0] == 2:
            print(f"{option_day} day(s), {option_month} month(s), {option_year} year(s) before was:",
                  test.subtract_from_date(days=option_day, months=option_month, years=option_year))
    else:
        print("Bye!")


def get_date():
    print("Chose add to date [1] or subtract from date date [2]?")
    choose = input(">>> ")

    option_day = input("How many day?: ")
    option_month = input("How many months?: ")
    option_year = input("How many year?: ")

    if choose == "1":
        return 1, option_day, option_month, option_year
    elif choose == "2":
        return 2, option_day, option_month, option_year
    else:
        print("Error!")
        get_date()


if __name__ == "__main__":
    main()
