class Group:
    group_data = {
        "group_name": "",
        "students": {}
    }

    def __init__(self, group_name, *args):
        for i in args:
            print(i.firstname)

        self.group_data["group_name"] = group_name

    def add_student(self, student):
        self.group_data["students"][student.scorebook["scorebook_number"]] = student
        return f"Student: {student.firstname} {student.surname} added."

    def all_students(self):
        return self.group_data["students"]
    pass


class Student:
    scorebook = {
        "scorebook_number": int()
    }

    def __init__(self, firstname, surname, scorebook_number):
        self.firstname = firstname
        self.surname = surname
        self.scorebook["scorebook_number"] = scorebook_number

    def set_score(self, subject, score):
        if subject in self.scorebook.keys():
            self.scorebook[subject].append(score)
        else:
            self.scorebook[subject] = []
            self.scorebook[subject].append(score)
        return self.scorebook[subject]

    def get_scores(self, subject):
        if subject in self.scorebook.keys():
            return f"Grades in {subject}: {self.scorebook[subject]}"
        else:
            return "Subject not found!"


def main():
    group = Group("ТВ-з11")

    print("\n\nAvailable operations:\n",
          "1: Add student;\n",
          "2: Add score;\n",
          "3: Get score;\n",
          "4: All Group list;\n")
    option = input("Make choice: ")
    option_variants = {"1": "Add student",
                       "2": "Add score",
                       "3": "Get score",
                       "4": "All Group list"}
    while option not in option_variants.keys():
        option = input("Wrong answer! Make choice: ")

    if option == "1":
        firstname = input("  Firstname: ")
        surname = input("  Surname: ")
        scorebook_number = input("  Scorebook_number: ")
        student = Student(firstname, surname, scorebook_number)
        print(group.add_student(student))
        main()
    elif option == "2":
        scorebook_number = input("  Student scorebook number: ")
        subject = input("  Subject: ")
        score = input("  Score: ")
        student = group.group_data["students"][scorebook_number]
        print(student.set_score(subject, score))
        main()
    elif option == "3":
        scorebook_number = input("  Student scorebook number: ")
        subject = input("  Subject: ")
        student = group.group_data["students"][scorebook_number]
        print(student.get_scores(subject))
        main()
    elif option == "4":
        for i in group.all_students():
            scorebook = group.all_students()[i].scorebook["scorebook_number"]
            print(f"Firstname: {group.all_students()[i].firstname}, "
                  f"Surname: {group.all_students()[i].surname}, "
                  f"Scorebook: {scorebook}")
        main()
    else:
        pass


if __name__ == "__main__":
    main()
